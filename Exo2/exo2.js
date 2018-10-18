
// Init MongoDB
const MongoClient = require("mongodb").MongoClient;

const url = "mongodb://localhost:27017/";
const dbKey = "matrix";


// Create graph
const graph = [
  { _id: "A", value: { adjlist: ["B", "C"], rank: 1 } },
  { _id: "B", value: { adjlist: ["C"], rank: 1 } },
  { _id: "C", value: { adjlist: ["A"], rank: 1 } },
  { _id: "D", value: { adjlist: ["C"], rank: 1 } }
];


// Connect MongoDB
MongoClient.connect(
	url,
	{ useNewUrlParser: true },
	function(err, db) {
		if (err) throw err;
		var matrixDb = db.db(dbKey);
		var collection = matrixDb.collection("graph");
		collection.deleteMany();

		// Insert collection in mongoDB
		collection.insertMany(graph, { w: 1 }).then(function(result) {

			// Map Function
			var map = function() {
				var adjlist = this.value.adjlist;
				var id = this._id;
				for (i = 0; i < adjlist.length; i++) {
					emit(adjlist[i], this.value.rank / adjlist.length);
				}
				emit(id, adjlist);
				emit(id, 0);
			};

			// Reduce Function
			var reduce = function(key, values) {
				const DAMPING_FACTOR = 0.85;

				var pageRank = 0.0;
				var adjlist = [];
				for (i = 0; i < values.length; i++) {
					if (values[i] instanceof Array) {
						adjlist = values[i]; // Si la valeur est du type array, alors elle représente la matrice d'adjacence qui va être utilisée pour la réinséertion dans MongoDB
					} else {
						pageRank += values[i]; // Sinon, c'est qu'elle représente le pagerank recalculé
					}
				}
				pageRank = 1 - DAMPING_FACTOR + DAMPING_FACTOR * pageRank;
				return { adjlist: adjlist, rank: pageRank };
			};

			function iterate(i) {
				collection.mapReduce(
					map,
					reduce,
					{
						out: {
							replace: "graph"
						}
					},
					function(err, result) {
						if (err) throw err;
						// Récupère les données en base pour afficher la progression des itérations
						collection
							.find()
							.toArray()
							.then(function(data) {
								console.log("iteration " + i, data);
								if (i < 20) {
									iterate(i + 1);
								} else {
									console.log("Fin du programme");
									db.close();
								}
							}
						);
					}
				);
			}
      iterate(0);
    });
  }
);
