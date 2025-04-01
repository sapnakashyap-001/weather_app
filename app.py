import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
API_KEY = os.getenv("API_KEY")       ##your_api_key_here##
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route('/', methods=['GET', 'POST'])
def weather():
    weather_data = None
    if request.method == 'POST':
        city = request.form['city']
        params = {'q': city, 'appid': API_KEY, 'units': 'metric'}
        response = requests.get(BASE_URL, params=params)
        if response.status_code == 200:
            weather_data = response.json()
        else:
            weather_data = {'error': 'City not found'}
    return render_template('weather.html', weather=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
