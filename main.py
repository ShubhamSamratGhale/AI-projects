import os
import requests
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv("DICTIONARY_API")

def get_meaning(word):
    url = f"{BASE_URL}/{word}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        meanings = data[0]["meanings"]
        for meaning in meanings:
            part = meaning["partOfSpeech"]
            definition = meaning["definitions"][0]["definition"]
            print(f"{part}: {definition}")
    else:
        print(f"Error {response.status_code}: Word not found")

def main():
    print("Dictionary Lookup")
    while True:         
        word = input("\nEnter a word (or type exit): ")
        if word.lower() == "exit":
            break
        get_meaning(word)

if __name__ == "__main__":
    main()
