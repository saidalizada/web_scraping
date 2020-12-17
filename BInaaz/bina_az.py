""" getting informations from real estate web site of the Azerbaijan"""
import bs4
import requests


def get_soup(url):
    """ get source of the web page """
    bina_az = bs4.BeautifulSoup(requests.get(url, {}).text, 'lxml')
    return bina_az

def get_price_and_name(bina_az):
    """ get price value, price currency and name of the home"""
    price_header = bina_az.find(name="div", attrs={"class": "price_header"})
    price_val = price_header.find(name="span", attrs={"class": "price-val"}).text
    price_cur = price_header.find(name="span", attrs={"class": "price-cur"}).text
    name = price_header.find('h1').text
    return price_val, price_cur, name

def get_parameters(bina_az):
    """ get parameters of the home"""
    parameters_list = []
    parameters_section = bina_az.find(name="div", attrs={"class": "parameters_section"})
    map_address = parameters_section.find(name="div", attrs={"class": "map_address"}).text
    parameters = parameters_section.find(name="table", attrs={"class": "parameters"})
    parameters_trs = parameters.find_all('tr')
    for parameters_tr in parameters_trs:
        par = parameters_tr.find_all('td')
        name = par[0].text
        val = par[1].text
        parameters_list.append((name, val))
    return map_address, parameters_list

def get_article(bina_az):
    """ get article of the home write by user """
    article = bina_az.find("article").text
    return article

if __name__ == "__main__":
    WEB_URL = 'https://bina.az/items/1500000'
    BINA_AZ = get_soup(WEB_URL)
    print(get_price_and_name(BINA_AZ))
