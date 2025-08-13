# Weather CLI App

A simple Python command-line application to fetch and display weather data using the [WeatherAPI](https://www.weatherapi.com/).
Supports location input in various formats, optional AQI data, and a 5-day weather forecast.

## Features

* Accepts location in multiple formats:

  * City name: `Delhi`
  * City + country: `Delhi, India`
  * Latitude + longitude: `28.6,77.2`
* Fetches current weather data from WeatherAPI.
* Optional Air Quality Index (AQI) data.
* Optional 5-day forecast.
* Saves raw JSON response to a file for reference.
* Built with an OOP structure for easy extension.

## Installation

1. Clone the repository:

   ```bash
   git clone <repo_url>
   cd <repo_name>
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your API key:

   * Sign up at [WeatherAPI](https://www.weatherapi.com/) and get your API key.
   * Create a `.env` file in the project root:

     ```
     WEATHER_API_KEY=your_api_key_here
     ```

## Usage

Basic command:

```bash
python app.py <location> <aqi: yes/no> <forecast: yes/no>
```

Examples:

```bash
python app.py "Delhi" no no
python app.py "Delhi, India" yes yes
python app.py "28.6,77.2" yes no
```

### Output

* Current weather with temperature and condition.
* Optional AQI data.
* Optional 5-day forecast.
* Saves API response as `weather_data.json` in the project directory.

## Error Handling

* If the location is invalid, the app will display a friendly error message instead of crashing.

## Example Output

```
Location: Delhi, India
Temperature: 31°C
Condition: Partly cloudy
AQI: PM2.5 - 45 μg/m³ (Moderate)
```

---