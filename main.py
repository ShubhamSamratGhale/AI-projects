import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_BASE = os.getenv("DICTIONARY_API")

def lookup_word(word):
    url = f"{API_BASE}/{word}"
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching word: {e}")
        return
    
    data = response.json()
    if not data:
        print("No data found")
        return
    
    print(f"\n'{word}':")
    
    for meaning in data[0].get('meanings', []):
        pos = meaning.get('partOfSpeech', '')
        defs = meaning.get('definitions', [])
        
        if defs:
            definition = defs[0].get('definition', '')
            print(f"  ({pos}) {definition}")

def main():
    print("Dictionary lookup - type 'quit' to exit")
    
    while True:
        word = input("Word: ").strip()
        
        if word.lower() in ['quit', 'q', 'exit']:
            break
            
        if not word or not word.isalpha():
            print("Enter a valid word")
            continue
            
        lookup_word(word.lower())

if __name__ == "__main__":
    main()
