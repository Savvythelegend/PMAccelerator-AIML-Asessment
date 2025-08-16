# Weather Application System - PM Accelerator Technical Assessment

This repository contains my implementation of both technical assessments for the AI Engineer Intern position at PM Accelerator. The project consists of two parts: a CLI-based Weather App (Task 1) and a full-featured Weather Tracking API with database integration (Task 2).

## Developer Information
- **Name**: [Your Name]
- **Position**: AI Engineer Intern Assessment
- **Company**: [PM Accelerator](https://www.linkedin.com/company/product-manager-accelerator/)

## Project Overview

### Task 1: CLI Weather Application
A command-line interface weather application that provides:
- Current weather information based on location input
- 5-day weather forecast
- Multiple location input formats support (City name, ZIP code, Coordinates)
- Real-time data from Weather API
- Current location detection

#### Key Features
- Interactive CLI interface
- Support for multiple location input formats
- Current weather conditions display
- 5-day forecast visualization
- Temperature, humidity, wind speed, and conditions display
- Error handling for invalid inputs

### Task 2: Weather Tracker API
A FastAPI-based weather tracking system with:
- Full CRUD operations
- Database persistence with Supabase PostgreSQL
- Advanced location validation
- Date range weather data
- RESTful API endpoints
- Web interface for easy interaction

#### Key Features
- **CREATE**: Store weather requests with location and date ranges
- **READ**: Retrieve historical weather data
- **UPDATE**: Modify stored weather requests
- **DELETE**: Remove weather records
- Date range validation
- Location verification
- Asynchronous weather data fetching
- Supabase PostgreSQL integration with row-level security

## Technology Stack

### Task 1 (CLI App)
- Python 3.8+
- Weather API integration
- Requests library
- Click for CLI interface
- Rich for terminal formatting

### Task 2 (Weather Tracker API)
- FastAPI
- Supabase PostgreSQL
- Pydantic
- Weather API Client
- HTML/JavaScript (Web Interface)
- Async HTTP Client (HTTPX)
- Supabase Client for Python

## Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Savvythelegend/PMAccelerator-AIML-Asessment.git
   cd PMAccelerator-AIML-Asessment
   ```

2. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env file with your:
   # - Weather API key
   # - Supabase URL
   # - Supabase API Key
   ```

3. Install dependencies:
   ```bash
   # For Task 1 (CLI App)
   cd Task1
   pip install -r requirements.txt

   # For Task 2 (Weather Tracker API)
   cd ../weather_tracker_api
   pip install -r requirements.txt
   ```

## Running the Applications

### Task 1: CLI Weather App
```bash
cd Task1
python app.py --location "London" --forecast
# or for current location
python app.py --current
```

### Task 2: Weather Tracker API
```bash
cd weather_tracker_api
cd src
uvicorn main:app --reload --host 0.0.0.0 --port 3000
```

Access the web interface at: http://localhost:3000
API documentation at: http://localhost:3000/docs

## API Endpoints (Task 2)

### Weather Requests
- `POST /requests` - Create new weather request
- `GET /requests` - List all weather requests
- `GET /requests/{request_id}` - Get specific request
- `PATCH /requests/{request_id}` - Update request
- `DELETE /requests/{request_id}` - Delete request

Example Request:
```json
{
  "user_name": "test_user",
  "location_input": "London",
  "start_date": "2025-08-16",
  "end_date": "2025-08-16"
}
```

## Demo Video

[View Demo Video](Insert your demo video link here)

The demo video showcases:
- CLI App usage and features
- Weather Tracker API endpoints
- Database operations
- Web interface interaction
- Error handling examples

## Additional Features

### Location Input Support
- City names
- ZIP/Postal codes
- GPS coordinates
- Landmarks
- Fuzzy matching for location names

### Data Validation
- Date range verification
- Location existence checking
- Input sanitization
- Error handling with meaningful messages

### Database Features
- Supabase PostgreSQL for robust data storage
- Row Level Security (RLS) policies
- Real-time subscriptions capability
- Efficient query handling with PostgREST
- Data persistence with automatic backups
- Transaction support
- Built-in authentication

## Security Considerations
- Input validation and sanitization
- Error handling without exposing sensitive information
- API key protection
- Rate limiting implementation

## 🤝 About PM Accelerator
[PM Accelerator](https://www.linkedin.com/company/product-manager-accelerator/) is a leading platform dedicated to accelerating the growth of product managers and tech professionals. The company focuses on providing hands-on experience and real-world projects to help individuals excel in their tech careers.

## 📄 License
This project is created as part of the PM Accelerator technical assessment and is available for review purposes.

## 🙏 Acknowledgments
- Weather data provided by WeatherAPI.com
- FastAPI framework
- SQLAlchemy ORM
- Python community
- PM Accelerator team for the opportunity
