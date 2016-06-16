from bs4 import BeautifulSoup
import json

soup = BeautifulSoup(open("verizon.html"),from_encoding="utf-8")

#print("'" + str(soup.encode("ascii")) + "'")

arr = []
response = [] #this stores the json

class prefPrice:

   def __init__(self, countryName, yesNo):
      self.countryName = countryName
      self.yesNo = yesNo

print "*******************"

for tr in soup.findAll('tr'):
	#print(tr)
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
		for child in countryName:
    			countryName = child
		response.append({'country': str(countryName), 'offered': yesNo})
	else:
		yesNo = tr.find('td', {'class': 'tr2 td22'})
		yesNo = str(yesNo)
	
		if "Yes" in yesNo:
			yesNo = "yes"
		elif "No" in yesNo:
			yesNo = "no"
		else:
			yesNo = "None"

		countryName = tr.find('td', {'class': 'tr2 td18'})
		str(countryName)

		if str(countryName) != "None":
			ountryName = countryName.find('p')
		
		if (str(countryName) != "None") and yesNo != "None":
			arr.append(prefPrice(countryName,yesNo))
			for child in countryName:
    				countryName = child
			response.append({'country': str(countryName), 'offered': yesNo})

print len(arr)
print json.dumps(response)
x = 0 #view the array of obejcts we built
while x < len(arr):
	prefPrice= arr[x]
	print prefPrice.countryName
	print prefPrice.yesNo
	x+=1
