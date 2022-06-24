from bs4 import BeautifulSoup
import requests

url = requests.get("https://www.cruzverde.cl/geniol-adultos-paracetamol-500-mg-20-comprimidos/260536.html")
soup = BeautifulSoup(url.content, "html.parser")
resultado = soup.find("span", {"class": "font-bold text-orange"})
precio_actual_text = resultado.text
precio_actual = float(precio_actual_text)
print(precio_actual)