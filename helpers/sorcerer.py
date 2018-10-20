from bs4 import BeautifulSoup
from requests import get
import helpers.tools as Tools


def get_all_sorcerer(start, end):
    sorcerer_array = []
    for index in range(start, end):
        print("Wrapper - Page", index, "on", end)
        url = "http://www.dxcontent.com/SDB_SpellBlock.asp?SDBID=" + str(index)
        r = get(url).text
        soup = BeautifulSoup(r, 'html.parser').find("div",{'class':'SpellDiv'})

        try:
            title = soup.find("div",{'class':'heading'}).find('p').get_text()
        except AttributeError:
            continue
        school = get_school(soup.find("p",{'class':'SPDet'}))
        level = get_level(soup.find("p",{'class':'SPDet'}))
        casting_time = get_casting_time(soup.findAll("p", {"class": "SPDet"})[1])
        components = get_component(soup.findAll("p", {"class": "SPDet"})[2])
        range_value = get_range(soup.findAll("p", {"class": "SPDet"})[3])
        effect = get_effect(soup.findAll("p", {"class": "SPDet"})[4])
        try:
            duration = get_duration(soup.findAll("p", {"class": "SPDet"})[5])
        except IndexError:
            duration = 'null'
        try:
            spell_resistance = get_spell_resistance(soup.findAll("p", {"class": "SPDet"})[6])
        except IndexError:
            spell_resistance = 'null'
        description = soup.find("div",{'class':'SPDesc'}).get_text()

        sorcerer = {
            "id": index,
            "title": title,
            "school": school,
            "level": level,
            "casting_time": casting_time,
            "components": components,
            "range_value": range_value,
            "effect": effect,
            "duration": duration,
            "spell_resistance": spell_resistance,
            "description": description
        }
        sorcerer_array.append(sorcerer)

    return sorcerer_array


def get_school(school):
    school = Tools.string_between_two_others('<b>School</b>', '<b>Level</b>', school)
    return school.strip().replace(";", "")


def get_level(level):
    sorcerer_level = Tools.string_between_two_others('sorcerer/wizard', ',', level)

    if "sorcerer/wizard" not in str(level):
        return 0

    return sorcerer_level.strip()[:1]


def get_casting_time(casting_time):
    return casting_time.get_text()


def get_component(component):
    component_value = Tools.string_between_two_others('<b>Components</b>', '</p>', component)
    return component_value


def get_range(range):
    range_value = Tools.string_between_two_others('<b>Range</b>', '</p>', range)
    return range_value


def get_effect(effect):
    effect_value = Tools.string_between_two_others('<b>Effect</b>', '</p>', effect)
    return effect_value


def get_duration(duration):
    duration_value = Tools.string_between_two_others('<b>Duration</b>', '</p>', duration)
    return duration_value


def get_spell_resistance(spell_resistance):
    spell_resistance_value = Tools.string_between_two_others('<b>Spell Resistance</b>', '</p>', spell_resistance)
    return spell_resistance_value
