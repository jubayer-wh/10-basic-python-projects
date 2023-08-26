import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Error: Failed to fetch the web page.")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    # Replace 'your-selector' with the CSS selector for the element you want to scrape.
    data = soup.select('your-selector')

    if not data:
        print("Error: No data found on the web page.")
        return

    # Extract and print the data.
    for item in data:
        print(item.text.strip())

if __name__ == "__main__":
    url = input("Enter the URL of the web page you want to scrape: ")
    scrape_website(url)
