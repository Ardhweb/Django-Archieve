from django.urls import path
from . import views


urlpatterns = [
    path('home/',views.home, name='home'),
    path('me',views.me, name="me"),
    
]
