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

level_forecast = sub_heading[2].find_all('td')
inflow_forecats = sub_heading[5].find_all('td')

if ( len(level_forecast) > 1 ):
	print( 'Flood (level) in state: ' + level_forecast[2].text )
else:
	print('No level flood forecast')

if( len(inflow_forecats) > 1 ):
	print( 'Flood (inflow) in state: ' + inflow_forecats[2].text )
else:
	print('No inflow flood forecats')

print('ENDFLOOD')

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

print('ENDCYCLONE')
