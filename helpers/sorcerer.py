from bs4 import BeautifulSoup
from requests import get


def get_all_sorcerer():
    url = "http://www.dxcontent.com/SDB_SpellBlock.asp?SDBID=1000"
    r = get(url).text
    soup = BeautifulSoup(r, 'html.parser').find("div",{'class':'SpellDiv'})

    title = soup.find("div",{'class':'heading'}).find('p').get_text()
    school = get_school(soup.find("p",{'class':'SPDet'}))

    return school


def get_school(school_string):
    start = '<b>School</b>'
    end = '<b>Level</b>'
    s = str(school_string)
    school = s[s.find(start)+len(start):s.rfind(end)]

    return school.strip()
