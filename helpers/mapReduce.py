from pprint import pprint


# TODO : Refactoring
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


def isVocalSpell(spell):
    if "V" not in spell['components'] :
        return False
    else:
        if "S" in spell['components'] or "F" in spell['components'] or "M" in spell['components']:
            return False
        else:
            return True


# TODO : Est-ce correct ? Est-ce utile ?
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

# TODO : Que faire ?
def _reduce(spells):
    y = []


# Filtre les sorts, retourne les sorts de niveau inférieur à 5 qui sont vocaux
def _filter(spells):
    y = []
    for x in spells:
        if isCorrectLevelSpell(x):
            if isVocalSpell(x):
                y.append(x)
    return y
