from django.shortcuts import render
import requests
import json

# Create your views here.

def home(request):  
    if request.method == 'POST':  
        city = request.POST.get('city', 'True')
        if city == "":
            city = "Pavlodar"
        
        source = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&APPID=<YOUR API KEY>').text
          
        list_of_data = json.loads(source)  
#        print(source)

        context = {  
            'city': city,  
            "country_code": str(list_of_data['sys']['country']),  
            "coordinate": str(list_of_data['coord']['lon']) + ' '  
                            + str(list_of_data['coord']['lat']),  
            "temp": str(list_of_data['main']['temp']),  
            "pressure": str(list_of_data['main']['pressure']),  
            "humidity": str(list_of_data['main']['humidity']),  
            "wind": str(list_of_data['wind']['speed']),  
        }  
    else:  
        context = {}  
       
    return render(request, 'index.html', context)   
