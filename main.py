import requests
from bs4 import BeautifulSoup
page = requests.get("https://www.autocentrum.pl/paliwa/ceny-paliw/")
soup = BeautifulSoup(page.content, 'html.parser')
price = soup.find(class_="table-responsive")
print(price.prettify())

items = price.find('td', class_='text-center').get_text()
items1 = items.replace('\n', '').replace('`', '') # jak dać ' w ""?
print(float(items1))


ceny_tags = price.select('.text-center .td')
ceny = [ct.get_text() for ct in ceny_tags]
print(ceny)