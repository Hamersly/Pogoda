from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm


def index(request):
    # appid = 'fddce6cfd000e398d5de994d461e332e'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=fddce6cfd000e398d5de994d461e332e'

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res["weather"][0]["icon"]
        }

        all_cities.append(city_info)
    # print(res.text)

    context = {'all_info': all_cities, 'form':form}

    return render(request, 'pogoda/index.html', context)
