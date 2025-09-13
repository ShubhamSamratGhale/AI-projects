import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("NASA_API_KEY")
BASE_URL = "https://api.nasa.gov/planetary/apod"

def get_apod():
    url = f"{BASE_URL}?api_key={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        title = data.get("title", "No title")
        date = data.get("date", "Unknown date")
        explanation = data.get("explanation", "No description available")
        image_url = data.get("url", "No image link")

        result = f"""
NASA Astronomy Picture of the Day
---------------------------------
Title: {title}
Date: {date}
Image URL: {image_url}

Explanation:
{explanation}
"""
        return result.strip()
    else:
        return f"Error: Could not fetch data ({response.status_code})"

def main():
    print("NASA Space Info App")
    print(get_apod())

if __name__ == "__main__":
    main()
