import requests
from datetime import date
import pandas as pd
from bs4 import BeautifulSoup
from csv import reader
from csv import writer
import csv


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


time_95 = pd.read_csv('C:\\Users\Tomek\PycharmProjects\scrapping\TIME\Time_95.csv')
new_column_95 = pd.DataFrame({today: F_95})
column_values_95 = pd.Series(F_95)
df_95 = pd.concat([time_95, new_column_95], axis=1)
df_95.to_csv('C:\\Users\Tomek\PycharmProjects\scrapping\TIME\Time_95.csv')

time_98 = pd.read_csv('C:\\Users\Tomek\PycharmProjects\scrapping\TIME\Time_98.csv')
new_column_98 = pd.DataFrame({today: F_98})
column_values_98 = pd.Series(F_98)
df_98 = pd.concat([time_98, new_column_98], axis=1)
df_98.to_csv('C:\\Users\Tomek\PycharmProjects\scrapping\TIME\Time_98.csv')

time_ON = pd.read_csv('C:\\Users\Tomek\PycharmProjects\scrapping\TIME\Time_ON.csv')
new_column_ON = pd.DataFrame({today: F_ON})
column_values_ON = pd.Series(F_ON)
df_ON = pd.concat([time_ON, new_column_ON], axis=1)
df_ON.to_csv('C:\\Users\Tomek\PycharmProjects\scrapping\TIME\Time_ON.csv')

time_ONN = pd.read_csv('C:\\Users\Tomek\PycharmProjects\scrapping\TIME\Time_ON+.csv')
new_column_ONN = pd.DataFrame({today: F_ONN})
column_values_ONN = pd.Series(F_ONN)
df_ONN = pd.concat([time_ONN, new_column_ONN], axis=1)
df_ONN.to_csv('C:\\Users\Tomek\PycharmProjects\scrapping\TIME\Time_ON+.csv')

time_LPG = pd.read_csv('C:\\Users\Tomek\PycharmProjects\scrapping\TIME\Time_LPG.csv')
new_column_LPG = pd.DataFrame({today: F_LPG})
column_values_LPG = pd.Series(F_LPG)
df_LPG = pd.concat([time_LPG, new_column_LPG], axis=1)
df_LPG.to_csv('C:\\Users\Tomek\PycharmProjects\scrapping\TIME\Time_LPG.csv')