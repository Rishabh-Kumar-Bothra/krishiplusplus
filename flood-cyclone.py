import requests
from bs4 import BeautifulSoup

'''FLOOD'''

url = 'http://india-water.gov.in/ffs/current-flood-forecast/'

try:
	r = requests.get(url,timeout=4)
except requests.exceptions.RequestException as error:
	print('Error Encountered : requests library')

soup = BeautifulSoup(r.text, 'lxml')
sub_heading = soup.find_all('tr')
level_forecast = sub_heading[2].text

if(level_forecast.find('No') != -1):
	print("No Flood Forecast")

else:
	print('Warning Flood: ' + sub_heading[2].text)

print('END1')

''' CYCLONE'''

url = 'http://www.rsmcnewdelhi.imd.gov.in/index.php?lang=en'
try:
	r = requests.get(url,timeout=4)
except requests.exceptions.RequestException as error:
	print('Error Encountered : requests library')

soup = BeautifulSoup(r.text, 'lxml')
sub_heading = soup.find_all('span')

ans = sub_heading[0].text

if ans.find('no') != -1:
	print('No Cyclone Forecast')

else:
	print('Warning Cyclone : ' + ans)

print('END2')
