from pprint import pprint

# Retourne true si le sort est le niveau du sort est inférieur ou égale à 4
def isCorrectLevelSpell(spell):
    str_level = spell['level']
    # Fix the error when level is equal to "" (can't be casted to int)
    if str_level == "":
        return False
    # Cast string level to int
    int_level = int(str_level)
    if int_level > 0 and int_level < 5:
        return True
    else:
        return False


# Retourne true si le sort est purement vocable, false sinon
def isVocalSpell(spell):
    if "V" not in spell['components'] :
        return False
    else:
        if "S" in spell['components'] or "F" in spell['components'] or "M" in spell['components']:
            return False
        else:
            return True


# Modifie les données en ne gardant que les données utiles
def _map(spells):
    y = []
    for x in spells:
        z = {
            "id": x['id'],
            "title": x['title'],
            "level": x['level'],
            "components": x['components'],
            "url": 'http://www.dxcontent.com/SDB_SpellBlock.asp?SDBID='+str(x['id'])
        }
        y.append(z)
    return y

# Filtre les sorts, retourne les sorts de niveau inférieur à 5 qui sont vocaux
def _reduce(spells):
    y = []
    for x in spells:
        if isCorrectLevelSpell(x):
            if isVocalSpell(x):
                y.append(x)
    return y
