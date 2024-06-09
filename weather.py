import requests

def get_weather(api_key, city):
    # URL to fetch the weather data
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"
    
    # Make the request to the OpenWeatherMap API
    response = requests.get(url)
    
    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()
        
        # Extract necessary data
        weather_main = data['weather'][0]['main']
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        
        # Determine the weather condition
        if weather_main.lower() in ["clear", "sunny"]:
            condition = "It's sunny."
        elif weather_main.lower() in ["rain", "drizzle"]:
            condition = "It's rainy."
        elif weather_main.lower() in ["snow"]:
            condition = "It's snowy."
        elif weather_main.lower() in ["clouds"]:
            condition = "It's cloudy."
        else:
            condition = f"The weather is {weather_description}."
        
        return {
            "temperature": temperature,
            "condition": condition
        }
    else:
        return {"error": "Unable to fetch the weather data"}

def main():
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    city = "Rexburg,ID"
    
    weather_info = get_weather(api_key, city)
    
    if "error" in weather_info:
        print(weather_info["error"])
    else:
        print(f"Current temperature in {city}: {weather_info['temperature']}°F")
        print(weather_info['condition'])

if __name__ == "__main__":
    main()
