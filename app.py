#make a virtual envirnment and install all the module 
#import the flask module
from flask import Flask,render_template,request
import requests
import datetime
from datetime import datetime
app = Flask(__name__)

#make a route and render all the html templates in this route
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        lon = request.form.get('lon')
        lat = request.form.get('lat')
       

        #take a variable to show the json data
        r = requests.get('https://api.openweathermap.org/data/2.5/forecast?lat='+lat+'&lon='+lon+'&appid=f8a324e35b73ef6a7f5a434b7a3df9b8&units=imperial')
       

       

        #read the json object
        json_object = r.json()

        print(json_object)
        
        #take some attributes like temperature,humidity,pressure of this 
        Htemperature = (round(json_object['list'][0]['main']['temp_max']))
        Ltemperature = float(round(json_object['list'][0]['main']['temp_min']))
        humidity = json_object['list'][0]['main']['humidity']
        pressure = json_object['list'][0]['main']['pressure']
        wind = json_object['list'][0]['wind']['speed']
        feels = (json_object['list'][0]['main']['feels_like'])
        presipitation =json_object['list'][0]['pop']*100
    
        condition = json_object['list'][0]['weather'][0]['main']
        description = json_object['list'][0]['weather'][0]['description']
        direction = json_object['list'][0]['wind']['deg']
        img = json_object['list'][0]['weather'][0]['icon']
        code = json_object['cod']
        #print(code)
        date =  json_object['list'][0]['dt']
        timestamp = datetime.fromtimestamp(date)
        time = timestamp.strftime('%a %b %d %Y')
        
        


        return render_template('home.html',Htemperature=Htemperature,json_object=json_object,img = img, time = time, lon = lon , lat = lat,
                               Ltemperature=Ltemperature,
                               pressure=pressure,code = code,
                               humidity=humidity,
                               condition=condition,
                               wind=wind,description=description, presipitation = presipitation,feels = feels,  direction = direction)
    else:
        return render_template('home.html') 

    
if __name__ == '__main__':
    app.run(debug=True)
