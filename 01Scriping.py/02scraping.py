import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://example.com"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Example: Extract all the links from the page
    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        print(href)
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")