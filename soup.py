from bs4 import BeautifulSoup

soup = BeautifulSoup(open("verizon.html"),from_encoding="utf-8")

print("'" + str(soup.encode("ascii")) + "'")

arr = []

class prefPrice:

   def __init__(self, countryName, yesNo):
      self.countryName = countryName
      self.yesNo = yesNo

print "*******************"

for tr in soup.findAll('tr'):
	print(tr)
	yesNo = "None"
	countryName = "None"
	yesNo = tr.find('td', {'class': 'tr0 td22'})
	yesNo = str(yesNo)
	
	if "Yes" in yesNo:
		yesNo = "yes"
	elif "No" in yesNo:
		yesNo = "no"
	else:
		yesNo = "None"

	countryName = tr.find('td', {'class': 'tr0 td18'})
	str(countryName)

	if str(countryName) != "None":
		countryName = countryName.find('p')

	if (str(countryName) != "None") and yesNo != "None":
		arr.append(prefPrice(countryName,yesNo))

	print yesNo
	print countryName

print len(arr)
