from pprint import pprint
import helpers.sorcerer as Sorcerer
import helpers.mapReduce as MapReduce

# Max number spell is 1976 (change to test as you wish)
data = Sorcerer.get_all_sorcerer(1, 1976)

# Map data
mapped = MapReduce._map(data)
# Filter data
filtered = MapReduce._filter(mapped)

# Write data in a file
with open('data.txt', 'w') as f:
    for item in filtered:
        f.write("%s\n" % item)
f.close()

# Print data
pprint(filtered)
