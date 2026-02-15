from fastapi import APIRouter
import httpx

# Create APIRouter for GET endpoints
router = APIRouter()

# Add a GET method to the "/" endpoint
@router.get("/")
def root():
    return {"message": "Hello from FastAPI!"}


# Define a GET API endpoint "/greet" with Query parameters
# In Browser, access the endpoint like this:
# "/greet?first_name=sarthak&last_name=bansal"
@router.get("/greet")
def greet(first_name: str, last_name: str):
    return {"message": f"Hello {first_name} {last_name}!"}


# Define a GET API endpoint "/hello" with Path parameters
# In Browser, access the endpoint like this: "/hello/Amar/Kumar"
@router.get("/hello/{fname}/{lname}")
def get_item(fname: str, lname: str):
    msg = "Hello! " + fname + " " + lname
    return {"message": msg}


# Define a GET API endpoint "/weather" that calls a free weather API
# In Browser, access like: "/weather?city=London" or "/weather?city=Delhi"
@router.get("/weather")
async def get_weather(city: str = "London"):
    """
    Fetch current weather data from Open-Meteo API (free, no API key required)
    Uses geocoding to convert city name to coordinates, then gets weather data
    """
    try:
        # Step 1: Convert city name to coordinates using Open-Meteo Geocoding API
        async with httpx.AsyncClient() as client:
            geo_response = await client.get(
                f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
            )
            geo_data = geo_response.json()
            
            if not geo_data.get("results"):
                return {"error": f"City '{city}' not found"}
            
            # Get coordinates of the first result
            location = geo_data["results"][0]
            lat = location["latitude"]
            lon = location["longitude"]
            city_name = location["name"]
            country = location.get("country", "Unknown")
            
            # Step 2: Get weather data using coordinates
            weather_response = await client.get(
                f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
            )
            weather_data = weather_response.json()
            current = weather_data["current_weather"]
            
            return {
                "city": city_name,
                "country": country,
                "temperature": f"{current['temperature']}°C",
                "windspeed": f"{current['windspeed']} km/h",
                "weather_code": current["weathercode"],
                "time": current["time"]
            }
    except Exception as e:
        return {"error": str(e)}
