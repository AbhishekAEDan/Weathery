from flask import Flask, render_template, request
import requests
import os
from datetime import datetime
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    updated = None
    temp_c = None
    temp_f = None

    if request.method == "POST":
        city = request.form.get("city", "").strip()
        if not city:
            weather = {"error": "Please enter a city name"}
            return render_template("index.html", weather=weather)

        # Call OpenWeatherMap API
        try:
            params = {"q": city, "appid": API_KEY, "units": "metric"}
            resp = requests.get(BASE_URL, params=params, timeout=8)
            data = resp.json()
        except requests.RequestException:
            weather = {"error": "Network error. Try again."}
            return render_template("index.html", weather=weather)

        # Check if city is valid
        cod = data.get("cod")
        if str(cod) != "200":
            message = data.get("message", "City not found")
            weather = {"error": message.capitalize()}
            return render_template("index.html", weather=weather)

        # Successful response
        weather = data
        updated = datetime.fromtimestamp(data.get("dt", int(datetime.now().timestamp()))).strftime("%I:%M %p")
        temp_c = int(round(data["main"]["temp"]))
        temp_f = int(round((temp_c * 9/5) + 32))


        return render_template(
            "index.html",
            weather=weather,
            updated=updated,
            temp_c=temp_c,
            temp_f=temp_f
        )

    # GET request (initial page load)
    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True)
