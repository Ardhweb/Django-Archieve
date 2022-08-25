from django.urls import path

from  .views import API
from . import views

urlpatterns = [
    path('api',API.as_view(), name="api"),
    
]
