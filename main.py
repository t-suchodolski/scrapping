import requests
from datetime import date
import pandas as pd
from bs4 import BeautifulSoup

page = requests.get("https://www.autocentrum.pl/paliwa/ceny-paliw/")
soup = BeautifulSoup(page.content, 'html.parser')
price = soup.find(class_="table-responsive")
items = price.find('td', class_='text-center').get_text()

#DISTRICTS
all_districts = []
list_dis =soup.find_all('a', {"class": "row-link"})
for args in list_dis:
    all_districts.append(args.text.strip())
#PRICES
all_prices= []
list_price = soup.find_all('td', {"class":"text-center"})
for prices in list_price:
    all_prices.append(float(prices.text.strip().replace(",",".")))
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
today = str(date.today())
archive_name = str('Fuel Price ' + today + '.csv')
print(archive_name)
df.to_csv(archive_name)




