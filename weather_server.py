from flask import Flask, request, render_template
import requests

app = Flask(__name__)

API_KEY = "your_api_key_here"  # Replace with a valid OpenWeatherMap API key

@app.route('/')
def index():
    return render_template('weather.html')

@app.route('/weather', methods=['GET'])
def weather():
    city = request.args.get('city', 'New York')
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url).json()

    # Check if the response is successful
    if response.get("cod") != 200:
        error_message = response.get("message", "Something went wrong.")
        return render_template('weather.html', error=error_message)

    weather_data = {
        "city": city,
        "temperature": response["main"]["temp"],
        "description": response["weather"][0]["description"],
        "humidity": response["main"]["humidity"],
        "wind_speed": response["wind"]["speed"]
    }

    return render_template('weather.html', weather_data=weather_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8083, debug=True)








