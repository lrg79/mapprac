from bs4 import BeautifulSoup
import json
import sys

class readPDF: 
	response = [] #this stores the json
	reload(sys)
	sys.setdefaultencoding('utf-8')
	soup = BeautifulSoup(open("verizon.html"),from_encoding="utf-8")

	def readTR(self, soup, num):

		for tr in soup.findAll('tr'):
			#print(tr)
			yesNo = "None"
			countryName = "None"
			classYesNo = ""
			classCountryCol = ""
			classYesNoCol = 'tr' + str(num) + ' ' + 'td22'
			yesNo = tr.find('td', {'class': classYesNo})
			yesNo = str(yesNo)
			
			if "Yes" in yesNo:
				yesNo = "yes"
			elif "No" in yesNo:
				yesNo = "no"
			else:
				yesNo = "None"
			classCountryCol = 'tr' + str(num) + ' ' + 'td18'
			countryName = tr.find('td', {'class': classCountryCol})
			str(countryName)

			if str(countryName) != "None":
				countryName = countryName.find('p')

			if (str(countryName) != "None") and yesNo != "None":
				for child in countryName:
		    			countryName = child
				self.response.append({'country': str(countryName), 'offered': yesNo})

	def printJSON(self):
		print(len(readPDF.response))
		print json.dumps(readPDF.response)
		
read = readPDF()
read.readTR(readPDF.soup,0)
read.readTR(readPDF.soup, 2)
read.printJSON()
