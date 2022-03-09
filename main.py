import requests
from bs4 import BeautifulSoup
page = requests.get("https://www.autocentrum.pl/paliwa/ceny-paliw/")
soup = BeautifulSoup(page.content, 'html.parser')
price = soup.find(class_="table-responsive")
#print(price.prettify())

items = price.find('td', class_='text-center').get_text()


def districts():
    all_districts = []
    list =soup.find_all('a', {"class": "row-link"})
    for args in list:
        all_districts.append(args.text.strip())
    print(all_districts)

def prices():
    all_prices= []
    chunk_size = 5
    grouped_prices = list()
    list_price = soup.find_all('a', {"class":"up"})
    for prices in list_price:
        all_prices.append(prices.text.strip())
    for i in range(0, len(all_prices), chunk_size):
        grouped_prices.append((all_prices[i:i+chunk_size]))
    print(grouped_prices)







def fueltype():
    fueltypes = []
    for fuel in soup.find_all('div', {"class":"fuel-logo pb"}):
        fueltypes.append(fuel.text.strip())
    for fuel in soup.find_all('div', {"class":"fuel-logo pbp"}):
        fueltypes.append(fuel.text.strip())
    for fuel in soup.find_all('div', {"class":"fuel-logo on"}):
        fueltypes.append(fuel.text.strip())
    for fuel in soup.find_all('div', {"class":"fuel-logo onp"}):
        fueltypes.append(fuel.text.strip())
    for fuel in soup.find_all('div', {"class":"fuel-logo lpg"}):
        fueltypes.append(fuel.text.strip())
    print(fueltypes)

districts()
prices()
fueltype()
