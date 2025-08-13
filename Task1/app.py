from dotenv import load_dotenv
import os
import requests
import json
import sys

# Load API key
load_dotenv()
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise ValueError("API_KEY is not set in .env file")


class WeatherApp:
    """Weather application to fetch current and forecast data from WeatherAPI.com"""

    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_current(self, location: str, aqi: str = "no") -> dict:
        """Fetch current weather data."""
        url = "http://api.weatherapi.com/v1/current.json"
        params = {"key": self.api_key, "q": location, "aqi": aqi}
        res = requests.get(url, params=params)
        if res.status_code == 200:
            return res.json()
        return {"error": f"Failed to retrieve data: {res.status_code}"}

    def get_forecast(self, location: str, days: int = 5) -> dict:
        """Fetch weather forecast data."""
        url = "http://api.weatherapi.com/v1/forecast.json"
        params = {"key": self.api_key, "q": location, "days": days}
        res = requests.get(url, params=params)
        if res.status_code == 200:
            return res.json()
        return {"error": f"Failed to retrieve data: {res.status_code}"}

    @staticmethod
    def save_json(data: dict, filename: str = "location.json"):
        """Save JSON data to a file."""
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)
        print(f"Data saved to {filename}")


if __name__ == "__main__":
    # CLI arguments
    loc = sys.argv[1] if len(sys.argv) > 1 else "London"
    aqi = sys.argv[2] if len(sys.argv) > 2 else "no"
    forecast_flag = sys.argv[3].lower() if len(sys.argv) > 3 else "no"

    if not loc.strip():
        print("Please provide a location (e.g., 'Delhi' or 'Delhi, India')")
        sys.exit(1)

    app = WeatherApp(API_KEY)

    # Current weather
    current_data = app.get_current(loc, aqi)
    if "error" not in current_data:
        cur = current_data.get("current", {})
        loc_name = current_data.get("location", {}).get("name", loc)
        country = current_data.get("location", {}).get("country", "")
        temp = cur.get("temp_c", "")
        cond = cur.get("condition", {}).get("text", "")

        print(f"Weather in {loc_name}{', ' + country if country else ''}: {temp}°C, {cond}")
        app.save_json(current_data)
    else:
        print(current_data["error"])
        sys.exit(1)

    # Optional forecast
    if forecast_flag in ["yes", "y", "true"]:
        try:
            forecast_data = app.get_forecast(loc, days=5)
            if "error" not in forecast_data:
                print("\n5-Day Forecast:")
                for day in forecast_data.get('forecast', {}).get('forecastday', []):
                    date = day.get('date', 'N/A')
                    cond = day.get('day', {}).get('condition', {}).get('text', 'N/A')
                    min_temp = day.get('day', {}).get('mintemp_c', 'N/A')
                    max_temp = day.get('day', {}).get('maxtemp_c', 'N/A')
                    print(f"{date}: {min_temp}°C - {max_temp}°C, {cond}")
            else:
                print(forecast_data["error"])
        except Exception as e:
            print(f"Error fetching forecast: {e}")


