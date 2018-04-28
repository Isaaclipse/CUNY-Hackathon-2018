from django.shortcuts import render
from django.http import HttpResponse
# import requests
import json
from .templatetags.shelter_tags import *
from django.conf import settings


# Create your views here.
def index(request):
    return render(request, 'sleepez/index.html')

def sign_up(request):
    return render(request, 'sleepez/sign_up.html')


def update(request):
    update_shelters()
    return HttpResponse('Shelters have been updated.')


def test(request):
    return render(request, 'sleepez/search.html')


def show_map(request, origin, destination):
    url = ('https://www.google.com/maps/embed/v1/directions?' +
           'key=AIzaSyClUKFNtktLHjlLPKsQIyU7RH0v8TDiTwI' +
           '&origin='+origin +
           '&destination=' + destination +
           '&mode=walking'
           )
    context_dict = {
        'url': url,
        'origin': origin,
        'destination':destination,
    }
    return render(request, 'sleepez/search.html', context_dict)


# def test(request):
#     # response = requests.get('https://data.cityofnewyork.us/resource/5ud2-iqje.json')
#     shelters_data = json.load(open('sleepez/static/data/shelters.json'))
#     shelters = {}

#     for shelter_data in shelters_data:
#         area = shelter_data["service_area"]
#         address = shelter_data['address']
#         shelters[area] = address

#     return render(request, 'sleepez/test.html', 
#         shelters
#         )

