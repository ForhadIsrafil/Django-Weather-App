from django.shortcuts import render
import requests
from . models import Cities
def weather(request):

	url         = 'http://api.openweathermap.org/data/2.5/weather?q={}&APPID=f7447d212a002af7623c1fb748233a6e'
	cities      = Cities.objects.all().order_by('-id')
	cities_data = []
	for city in cities:
		w    = requests.get(url.format(city)).json()
		f    = w['main']['temp']
		c    = int((f-245)/1.8)
		city_weather = {
		'city': city,
		'tempreture': c,
		'description': w['weather'][0]['description'],
		'icon': w['weather'][0]['icon'],
		'wind': w['wind']['speed'],
		}
		cities_data.append(city_weather)
	context2 = {'cities_data': cities_data}

	if request.method == 'POST':
		city_name = request.POST['city']
		try:
			w    = requests.get(url.format(city_name)).json()
			f    = w['main']['temp'] #fahrenheit
			c    = int((f-245)/1.8)  #celsius 
			one_city = {
			'city': city_name,
			'tempreture': c,
			'description': w['weather'][0]['description'],
			'icon': w['weather'][0]['icon'],
			'wind': w['wind']['speed'],
			}
			context1 = {'one_city': one_city,'cities_data': cities_data}
			return render(request,'weather.html',context1)
		except Exception:
			return render(request,'weather.html',context2)

	return render(request,'weather.html',context2)

	return render(request,'weather.html',context2)
