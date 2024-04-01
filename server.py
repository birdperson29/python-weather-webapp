from flask import Flask, render_template, request
from weather import get_curr_weather
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index(): 
    return render_template('index.html')

@app.route('/weather')
def get_weather(): 
    city = request.args.get('city')
    if not bool(city.strip()): 
        city = "Delhi"
    weather_data = get_curr_weather(city)
    
    if not weather_data['cod']==200: 
        return render_template('city-not-found.html')
    temp_celsius = weather_data['main']['temp'] - 273.15
    feels_like_celsius = weather_data['main']['feels_like'] - 273.15
    return render_template('weather.html', title=weather_data["name"], status=weather_data["weather"][0]["description"].capitalize(), 
                           temp=f"{temp_celsius:.1f}", 
                           feels_like=f"{feels_like_celsius:.1f}",
                           )

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)