from bs4 import BeautifulSoup

soup = BeautifulSoup(open("verizon.html"),from_encoding="utf-8")

print("'" + str(soup.encode("ascii")) + "'")

accepted = []
country = []

prefPrice = soup.findAll('td', {'class': 'tr0 td22'})
countries = soup.findAll('td', {'class': 'tr0 td18'})

accepted.extend(prefPrice)
country.extend(countries)

prefPrice = soup.findAll('td', {'class': 'tr0 td22'})
countries = soup.findAll('td', {'class': 'tr0 td18'})

accepted.extend(prefPrice)
country.extend(countries)

print accepted
print len(accepted)
print country
print len(country)