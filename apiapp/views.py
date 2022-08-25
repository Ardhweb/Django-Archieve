from django.shortcuts import render

# Create your views here.
from .get_data import api_data
from django.views.generic import TemplateView

class API(TemplateView):
    template_name = 'api.html'
    def get_context_data(self, *args, **kwargs):
        context = {
            'drops' : api_data(),}
        return context