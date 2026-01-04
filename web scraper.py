import requests
from bs4 import BeautifulSoup
import csv
import json
import time

URL = "https://news.ycombinator.com/"   # Example news website
HEADERS = {"User-Agent": "Mozilla/5.0"}
DELAY = 3  # seconds
KEYWORD = ""  # set keyword like "AI" or leave empty

def fetch_headlines():
    try:
        response = requests.get(URL, headers=HEADERS, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print("Error fetching website:", e)
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    headlines = []

    for item in soup.select(".titleline a"):
        title = item.text
        link = item["href"]

        if KEYWORD.lower() in title.lower():
            headlines.append({
                "title": title,
                "url": link,
                "time": "Not Available"
            })

    return headlines

def save_to_csv(data):
    with open("headlines.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "url", "time"])
        writer.writeheader()
        writer.writerows(data)

def save_to_json(data):
    with open("headlines.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def main():
    print("Fetching headlines...")
    headlines = fetch_headlines()

    if not headlines:
        print("No headlines found.")
        return

    save_to_csv(headlines)
    save_to_json(headlines)

    print(f"{len(headlines)} headlines saved successfully!")
    time.sleep(DELAY)

if __name__ == "__main__":
    main()
