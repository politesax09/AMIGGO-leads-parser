from chepy import Chepy
import quopri
import urllib
from bs4 import BeautifulSoup
f = open("./salida.txt","r")
# print(f.read())
# print(Chepy(f.read()).affine_decode().o)
entrada = f.read()
salida = urllib.parse.unquote(quopri.decodestring(entrada).decode("utf-8",errors="ignore"))
print(salida)
soup = BeautifulSoup(salida,"html.parser")

results = {}
for elem in soup.find_all("li"):
    if "fecha" in elem.text.lower():
        results["fecha"] = elem.text.split(": ")[1]
    elif "código" in elem.text.lower():
        results["codigo"] = elem.text.split(": ")[1]
    elif "producto" in elem.text.lower():
        results["producto"] = elem.text.split(": ")[1]

results["url"] = soup.find("a").attrs["href"].split("url=")[1].split("&")[0]

print(results)