from django.shortcuts import render
import math
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method  == 'POST':
        city = request.POST['city']
        reqst = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=4f44cb852c5009baee74a0832be7b412&units=metric').read()
        json_data = json.loads(reqst)
        data = {
            "name": str(json_data['name']),
            "country_code": str(json_data['sys']['country']),
            "timezone": math.trunc(json_data['timezone']/3600),
            "sunrise": (int(json_data['sys']['sunrise'])/3600),
            "sunset": (int(json_data['sys']['sunset'])/3600),
            "coordinate": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp'])+' \u2103',
            "feels_like": str(json_data['main']['feels_like'])+' \u2103',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
        }
    else:
        data = {}
    return render(request, 'index.html', data)

