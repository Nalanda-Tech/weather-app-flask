import requests
import json
from flask import Flask,render_template, request


app=Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == "POST":
    	city = request.form['city']
    	api_key = "870095279633b0570e19250d31ee5e74"

    	if city:
    		weather_url = requests.get(
	            f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city}&units=imperial')
    		weather_data = weather_url.json()
    		temp = round(weather_data['main']['temp'])
    		humidity = weather_data['main']['humidity']
    		wind_speed = weather_data['wind']['speed']
    		return render_template("result.html", temp=temp, humidity=humidity, wind_speed=wind_speed, city=city)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)