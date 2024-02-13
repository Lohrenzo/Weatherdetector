from django.shortcuts import render
import math
import json
import urllib.request
import urllib.parse
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method  == 'POST':
        city = request.POST['city']
        encoded_city = urllib.parse.quote(city)
        try:
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
        except:
            messages.info(request, "City Not Found")
            data = {}
        # except urllib.error.HTTPError as e:
        #     return HttpResponse(f'HTTP Error: {e.code} {e.reason}')
    else:
        data = {}
    return render(request, 'index.html', data)

