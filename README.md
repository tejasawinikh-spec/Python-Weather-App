# Python Weather App

## Project Overview
A Python-based Weather Application that retrieves real-time weather information and a 5-day forecast for any city using the OpenWeather API.

## Features
- Search weather by city name.
- Display current temperature in Celsius.
- Display humidity and weather conditions.
- Display wind speed.
- Show a 5-day weather forecast.
- Handle invalid city names.
- Handle API and connection errors.
- Secure API key management using environment variables.

## Technologies Used
- Python
- OpenWeather API
- Requests
- JSON
- Python-dotenv

## Project Structure

```text
Weather-App/
│
├── main.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## Installation

1. Clone the repository.
2. Create and activate a Python virtual environment.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project folder and add:

```text
OPENWEATHER_KEY=your_api_key
```

5. Run the application:

```bash
python main.py
```

## API Key Security
The API key is stored in a `.env` file and is excluded from GitHub using `.gitignore`. Users must provide their own OpenWeather API key.

## Author
Tejaswini Krishna Hulswar