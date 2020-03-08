from django.shortcuts import render
# from .models import DustStats
from urllib.request import urlopen
from django.views.generic import TemplateView
import json
# Create your views here.

def index(request):
    return render(request, 'base.html')

class DustbinSatsView(TemplateView):
    # model = DustStats
    template_name = 'dustbinStats.html'

    def get_context_data(self, **kwargs):
        READ_API_KEY = 'AP6S7R81XD7O3T75'
        CHANNEL_ID = '1012728'

        connection = urlopen("http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s" %(CHANNEL_ID, READ_API_KEY))
        response = connection.read()
        data = json.loads(response)

        context = super().get_context_data(**kwargs)
        context['field1'] = 0 if not data['field1'] else data['field1']
        context['field2'] = 0 if not data['field2'] else data['field2']
        context['field3'] = 0 if not data['field3'] else data['field3']
        
        return context

