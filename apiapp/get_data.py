


import requests

def api_data():
    url = 'https://anime-facts-rest-api.herokuapp.com/api/v1'
    r = requests.get(url)
    data = r.json()
    data_list = []
    for i in range(len(data['data'])):
        data_list.append(data['data'][i])
    return data_list