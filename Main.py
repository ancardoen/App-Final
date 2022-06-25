import requests
from bs4 import BeautifulSoup


URL = "https://www.cruzverde.cl/search?query=paracetamol"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find_all("span", {"class": ["font-bold", "text-orange"]})
print(results)

