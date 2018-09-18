from bs4 import BeautifulSoup
from requests import get


def get_all_sorcerer():
    url = "http://www.dxcontent.com/SDB_SpellBlock.asp?SDBID=1000"
    r = get(url).text
    soup = BeautifulSoup(r, 'html.parser')
    title = soup.find("div",{'class':'heading'}).find('p').get_text()
    return title
