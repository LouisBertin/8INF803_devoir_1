from bs4 import BeautifulSoup
from requests import get
import helpers.tools as Tools


def get_all_sorcerer():
    url = "http://www.dxcontent.com/SDB_SpellBlock.asp?SDBID=1000"
    r = get(url).text
    soup = BeautifulSoup(r, 'html.parser').find("div",{'class':'SpellDiv'})

    title = soup.find("div",{'class':'heading'}).find('p').get_text()
    school = get_school(soup.find("p",{'class':'SPDet'}))
    level = get_level(soup.find("p",{'class':'SPDet'}))
    casting_time = get_casting_time(soup.findAll("p", {"class": "SPDet"})[1])
    components = get_component(soup.findAll("p", {"class": "SPDet"})[2])

    return components


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
    component_value = Tools.string_between_two_others('<b>Components</b>', '(', component)
    return component_value
