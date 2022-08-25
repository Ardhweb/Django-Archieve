from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from .models import APIMODEL
from . import api_get


def index(request):
    return HttpResponse("Hello Index is Here")

def apidata(request):
    x_val = api_get.name_list
    for i in range(0,5):
        value = APIMODEL(
            name = x_val[i],
        )
        value.save()
    data = APIMODEL.objects.all()
    return render(request, 'api.html', {'data':data,})
