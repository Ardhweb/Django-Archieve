from multiprocessing import context
from urllib import response
from wsgiref.util import request_uri
from django.shortcuts import render

# Create your views her

import requests
import json


url = 'https://anime-facts-rest-api.herokuapp.com/api/v1'
myresponse = requests.get(url).json
# print(myresponse)



# animelist = []

# def get_data():
#     for e in range(0,5):
#         # id = myresponse['data'][e]['anime_id'],
#         name = myresponse['data'][e]['anime_name']
#         # animelist.append(id)
#         animelist.append(name)
       
#         print(f"{id}:{name}")

       
# get_data()  

# print(animelist)




def home(request):
    url = 'https://anime-facts-rest-api.herokuapp.com/api/v1'
    myresponse = requests.get(url).json()
   
    print(myresponse)
    data = {
        'anime_id':myresponse['data'][0]['anime_id'],
        'anime_name':myresponse['data'][0]['anime_name'],
        'anime_img':myresponse['data'][0]['anime_img'],
    }
  

    context = {'myresponse':myresponse, 'data':data, }

    return render(request,'home.html',context )
























    
def me(request):
    url = 'https://anime-facts-rest-api.herokuapp.com/api/v1'
    myr = requests.get(url).json()

    lista = []
  

    for  i in range(0,4):
        y = myr['data'][i]['anime_name']
        lista.append(y)
        print (y)

    context = {'myr':myr, 'y':y }

    return render(request,'ge.html',context )
