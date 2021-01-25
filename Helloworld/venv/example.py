import requests
from requests.auth import HTTPBasicAuth
from Key import *
from requests_oauthlib import OAuth1
from requests_oauthlib import OAuth2
import oauth2
import json
'''
auth_data = {
    'grant_type': 'client_credentials'
}
response = requests.post('https://api.twitter.com/oauth2/token',data= auth_data,auth=HTTPBasicAuth(ApiKey,Apisecretkey))
print(response.status_code)
print(response.text)
auth = (response.json())
print(response.headers)

my_headers = {'Authorization' : 'Bearer '+access_token}
print(my_headers.get('Authorization'))
response = requests.get('https://api.twitter.com/2/tweets/compliance/jobs', headers=my_headers)
print(response.status_code)

from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

clientKey = ApiKey
clientSecret = Apisecretkey
requestTokenUrl = 'https://api.twitter.com/oauth2/token'

clientObject = BackendApplicationClient(client_id=clientKey)
oauth = OAuth2Session(client=clientObject)
accessToken = oauth.fetch_token(token_url=requestTokenUrl, client_id=clientKey, client_secret=clientSecret)
# access token should be cached/saved and used repeatedly rather than making many requests fo a new token
print(accessToken)

resourceUrl = 'https://api.twitter.com/labs/2/users/by?'
paramDict = {"usernames": "@sraghavan8007",}
bearerAccessToken = 'AAAAAAAAAAAAAAAAAAAAAHE%2BLQEAAAAASrqrXT%2BdQODb3iDupQUsQfjGtWY%3Di5LuKYzGAz5BcJIrEeT04Rz21hyV4LiFj8nZKEAY2oWwNnvDLV'
r = requests.get(resourceUrl, headers={'Authorization' : 'Bearer '+ bearerAccessToken},params = paramDict)
data = r.status_code
print(data)



states = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
params={'appid':'0bc091ddf3377bde8cd618cf9b043162'}
for state in states:
    url = 'https://api.openweathermap.org/data/2.5/weather?q=' + state + ''
    responses = requests.get(url=url, params=params)
    if(responses.status_code ==404):
        print('please enter a valid city{}'.format(state))
    else:
        with open('wheather.json', 'a') as f:
            json.dump(responses.json(), f, indent=4, )

'''
url = "https://community-open-weather-map.p.rapidapi.com/weather"
querystring = {"q":"London"}
headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "c27a0ba597mshb5c1efb9b897c9cp196459jsn56a63db88c77"
    }
response = requests.get( url = url, headers=headers,params =querystring )
str = (response.text)
jl = (json.loads(str))
print(jl['weather'][0]['description'])



dic = {'mobilename':['nokia','samsung','motorola']}
for i in dic['mobilename']:
    print(i)
