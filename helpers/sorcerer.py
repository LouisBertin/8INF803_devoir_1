from bs4 import BeautifulSoup
from requests import get


def get_all_sorcerer():
    url = "http://www.dxcontent.com/SDB_SpellBlock.asp?SDBID=1000"
    r = get(url).text
    soup = BeautifulSoup(r, 'html.parser').find("div",{'class':'SpellDiv'})

    title = soup.find("div",{'class':'heading'}).find('p').get_text()
    school = get_school(soup.find("p",{'class':'SPDet'}))
    level = get_level(soup.find("p",{'class':'SPDet'}))
    casting_time = get_casting_time(soup.findAll("p", {"class": "SPDet"})[1])

    return level


def get_school(school):
    start = '<b>School</b>'
    end = '<b>Level</b>'
    s = str(school)
    school = s[s.find(start)+len(start):s.rfind(end)]
    return school.strip().replace(";", "")


def get_level(level):
    start = 'sorcerer/wizard'
    end = ','
    s = str(level)
    sorcerer_level = s[s.find(start)+len(start):s.rfind(end)]

    if "sorcerer/wizard" not in s:
        return 0

    return sorcerer_level.strip()[:1]


def get_casting_time(casting_time):
    return casting_time.get_text()
