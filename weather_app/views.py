from django.shortcuts import render, redirect
import requests

def weather(request):
	if request.method == "POST":
		try:
			city=request.POST.get("city")
			a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"
			a2 = "&q=" + city
			a3 = "&appid=" + "c6e315d09197cec231495138183954bd"
			wa = a1 + a2 + a3
			
			res = requests.get(wa)
			data = res.json()
			print(data)
		
			id = data['weather'][0]['id']
			if id<300 and id>=200:
				weatherImg = "https://img-premium.flaticon.com/png/512/2036/premium/2036041.png?token=exp=1632633336~hmac=9ffba05cb7cac3fc91780a17e8b5fc55"#thunderstorm
			if id<400 and id>=300:
				weatherImg = "https://img-premium.flaticon.com/png/512/1207/premium/1207621.png?token=exp=1632633402~hmac=32e1aca974f0f802523990e34316616b"#drizzle
			if id<600 and id>=500:
				weatherImg="https://img-premium.flaticon.com/png/512/1208/premium/1208475.png?token=exp=1632633359~hmac=220624071a768fd88272aa52eb0a4cf5"#rain
			if id<700 and id>=600:
				weatherImg="https://img-premium.flaticon.com/png/512/1207/premium/1207557.png?token=exp=1632633448~hmac=349b95d469a8ea2247da49f08bff789d"#snow
			if id<800 and id>=700:
				weatherImg="https://img-premium.flaticon.com/png/512/1207/premium/1207589.png?token=exp=1632633529~hmac=7dfb0c86642816ae3415f1772a31afd7"#ATMOSPHERE
			if id==800:
				weatherImg="https://img-premium.flaticon.com/png/512/1207/premium/1207545.png?token=exp=1632633565~hmac=d732e6c81cd2acf1386b0516deb7cf49"#CLEAR
			if id<900 and id>800:
				weatherImg="https://img-premium.flaticon.com/png/512/1207/premium/1207546.png?token=exp=1632633626~hmac=cde42697f27f99c8d5f133b08e0c8795"#CLOUDS

			weather = "Weather: " +str(data['weather'][0]['main'])
			temp = "Temperature: " + str(data['main']['temp']) + " °C"
			feel_temp = "Feels Like: " + str(data['main']['feels_like']) + " °C"
			min_temp = "Min Temperature: " + str(data['main']['temp_min']) + " °C"
			max_temp = "Max Temperature: " + str(data['main']['temp_max']) + " °C"
			humidity = "Humidity: "  + str(data['main']['humidity'])
			icon = data['weather'][0]['icon']
			icon = "http://openweathermap.org/img/w/"+ icon + ".png"
			city = city.title()
			return render(request, "weather.html", {"temp":temp, "icon":icon, "weather":weather, "feel_temp":feel_temp, "min_temp":min_temp, "max_temp":max_temp, "humidity": humidity, "city":city, "weatherImg":weatherImg})
		except Exception as e:
			msg = "ISSUE" + str(e)
			return render(request, "weather.html", {"temp":msg})
	else:
		return render(request,"weather.html")
