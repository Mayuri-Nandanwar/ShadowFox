#import libraries
import requests
from bs4 import BeautifulSoup

#website link
URL = "https://ghrce.raisoni.net"

#send request to webpage
result = requests.get(URL)

#analyze the HTML content
soup = BeautifulSoup(result.text, "html.parser")

#find all h2 headings
headings = soup.find_all("h2")

#print the data
print("Headlines from the webpage :\n")

for item in headings:
    print(item.text.strip())