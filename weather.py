from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_curr_weather(city="Delhi"): 
    
    request_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv('API_KEY')}"
    
    weather_data = requests.get(request_url).json()
    
    return weather_data

if __name__ == "__main__":
    print('\n*** Get Weather Conditions! ***\n')
    
    city = input("\nEnter city name: ")
    
    if not bool(city.strip()): 
        city = "Delhi"
    
    weather_data = get_curr_weather(city)
    print('\n')
    pprint(weather_data)
    
    