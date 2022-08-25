


import requests


def home(request):
    url = 'https://anime-facts-rest-api.herokuapp.com/api/v1'
    response = requests.get(url)
  
    anime_data = response.json()
    for e in anime_data:
        print(e)
   
home()