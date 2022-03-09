import requests
from datetime import date
import pandas as pd
from bs4 import BeautifulSoup
page = requests.get("https://www.autocentrum.pl/paliwa/ceny-paliw/")
soup = BeautifulSoup(page.content, 'html.parser')
price = soup.find(class_="table-responsive")
items = price.find('td', class_='text-center').get_text()
#print(price.prettify())


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
    #print(grouped_prices)

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

#districts()
#prices()
#fueltype()

#DISTRICTS
all_districts = []
list_dis =soup.find_all('a', {"class": "row-link"})
for args in list_dis:
    all_districts.append(args.text.strip())
#PRICES
all_prices= []
list_price = soup.find_all('td', {"class":"text-center"})
for prices in list_price:
    all_prices.append(prices.text.strip())
F_95 = (all_prices[0::5])
F_98 = (all_prices[1::5])
F_ON = (all_prices[2::5])
F_ONN = (all_prices[3::5])
F_LPG = (all_prices[4::5])


data = {'District': all_districts,
        '95': F_95,
        '98': F_98,
        'ON': F_ON,
        'ON+': F_ONN,
        'LPG': F_LPG
        }
df = pd.DataFrame(data)
#print(df)
today = str(date.today())
archive_name = str('Fuel Price ' + today + '.csv')
print(archive_name)
df.to_csv(archive_name)

