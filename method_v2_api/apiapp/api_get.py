import json
import requests

name_list = []
resp = requests.get('https://anime-facts-rest-api.herokuapp.com/api/v1')
data = resp.json()
#print(data[1]['league'])

for i in range(0,12):
    x = data['data'][i]['anime_name']
    name_list.append(x)
    print(x,end=' ')
    #print(y)