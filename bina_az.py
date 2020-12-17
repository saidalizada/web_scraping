import bs4
import requests
import lxml.etree as xml
url  = 'https://bina.az/items/1500000'
soup = bs4.BeautifulSoup(requests.get(url, {}).text, 'lxml')

def get_price_and_name(soup):
    price_header = soup.find(name="div", attrs = {"class": "price_header"})
    price_val = price_header.find(name="span", attrs = {"class": "price-val"}).text
    price_cur = price_header.find(name="span", attrs = {"class": "price-cur"}).text
    name = price_header.find('h1').text
    return price_val, price_cur, name

def get_parameters(soup):
    parameters_list = []
    parameters_section = soup.find(name="div", attrs = {"class": "parameters_section"})
    map_address = parameters_section.find(name="div", attrs = {"class": "map_address"}).text
    parameters = parameters_section.find(name="table", attrs = {"class": "parameters"})
    parameters_trs = parameters.find_all('tr')
    for parameters_tr in parameters_trs:
        par = parameters_tr.find_all('td')
        name = par[0].text
        val = par[1].text
        parameters_list.append((name,val))
    return map_address,parameters_list

def get_article(soup):
    article = soup.find("article").text
    return article


if __name__ == "__main__":
    print(get_price_and_name(soup))
