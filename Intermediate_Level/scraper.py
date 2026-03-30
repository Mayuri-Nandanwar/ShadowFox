#Web Scraper: Extract data from websites using libraries like Beautiful Soup or Scrapy

# importing required libraries
import requests
from bs4 import BeautifulSoup

# website link (you can change this)
url = "https://www.bbc.com"

# sending request to the website
response = requests.get(url)

# parsing the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# extracting all headings (h2 tags)
headings = soup.find_all("h2")

# printing the extracted data
print("Headlines from the website:\n")

for h in headings:
    print(h.text.strip())