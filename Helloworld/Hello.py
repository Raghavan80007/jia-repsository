
credentials={}
credentials['CONSUMER_KEY'] ="0fmWWXEgEwtfor6nYkmn48PXB"
credentials['CONSUMER_SECRET'] ="XpRGfuQvHW3JtSxEd6ROe1INU0d4HQRK1VxdFuA7SjO82ZqKSj"
credentials['ACCESS_TOKEN'] ="1346788790254202880-hErqexJsBrxoZyw8xGLLsUyujjuE3T"
credentials['ACCESS_SECRET'] ="C0yvF8r4PU8C5UuGqeuvklDBgHW5j0esutieAPCxMw15b"

base_url = 'https://api.twitter.com/'
auth_url = '{}oauth2/token'.format(base_url)
import requests
from requests.auth import HTTPBasicAuth

auth_data = {
    'grant_type': 'client_credentials'
}
res = requests.post(url=auth_url ,auth=HTTPBasicAuth('0fmWWXEgEwtfor6nYkmn48PXB', 'XpRGfuQvHW3JtSxEd6ROe1INU0d4HQRK1VxdFuA7SjO82ZqKSj'),data = auth_data)
print (res.text)
ress = res.json()



