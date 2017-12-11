import requests
from bs4 import BeautifulSoup
import simplejson as json

# This is the url to which the query is made
url_hasura = "https://data.combatant32.hasura-app.io/v1/query"

# This is the json payload for the query
requestPayload = {
    "type": "update",
    "args": {
        "table": "krishiplusplus",
        "where": {
            "state": {
                "$eq": "Gujarat"
            }
        },
        "$set": {
            "flood": "No Flood Prediction",
            "cyclone": "No Cyclone Preediction"
        }
    }
}

# Setting headers
headers = {
    "Content-Type": "application/json",
    "Authorization": "Authorization Token"
}

'''FLOOD'''

url = 'http://india-water.gov.in/ffs/current-flood-forecast/'

try:
	r = requests.get(url,timeout=4)
except requests.exceptions.RequestException as error:
	print('Error Encountered : requests library')

soup = BeautifulSoup(r.text, 'lxml')
sub_heading = soup.find_all('tr')

level_forecast = sub_heading[2].find_all('td')
inflow_forecast = sub_heading[5].find_all('td')

if ( len(level_forecast) > 1 ):
	print( 'Flood (level) in state: ' + level_forecast[2].text )

	requestPayload["args"]["where"]["state"]["$eq"] = level_forecast[2].text
	requestPayload["args"]["$set"]["flood"] = 'Warning: Flood (level) Prediction'
else:
	print('No level flood forecast')

if( len(inflow_forecast) > 1 ):
	print( 'Flood (inflow) in state: ' + inflow_forecast[2].text )

	requestPayload["args"]["where"]["state"]["$eq"] = inflow_forecast[2].text
	requestPayload["args"]["$set"]["flood"] = 'Warning: Flood (inflow) Prediction'
else:
	print('No inflow flood forecast')

print('\nsending flood update request')
resp = requests.request("POST", url_hasura, data=json.dumps(requestPayload), headers=headers)
print(resp.content)

print('\nENDFLOOD\n')

''' CYCLONE'''

newurl = 'http://www.rsmcnewdelhi.imd.gov.in/index.php?lang=en'

try:
	r = requests.get(newurl,timeout=4)
except requests.exceptions.RequestException as error:
	print('Error Encountered : requests library')

soup = BeautifulSoup(r.text, 'lxml')
sub_heading = soup.find_all('span')

ans = sub_heading[0].text

if ans.find('no') != -1:
	print('No Cyclone Forecast')

else:
	CylonerequestPayload = {
    	"type": "update",
    	"args": {
        	"table": "krishiplusplus",
        	"where": {},
        	"$set": {
            	"cyclone": "No cyclone prediction"
        	}
    	}
	}
	print('Warning Cyclone : ' + ans)

	requestPayload["args"]["$set"]["cyclone"] = ans
	print('\nsending cyclone update request')
	resp = requests.request("POST", url_hasura, data=json.dumps(CylonerequestPayload), headers=headers)
	print(resp.content)
	

print('\nENDCYCLONE\n')
