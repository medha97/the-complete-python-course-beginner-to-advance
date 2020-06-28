from bs4 import BeautifulSoup
import requests

search = input("Enter search terms:")
params = {"q": search}
r = requests.get("https://www.bing.com/search", params = params)

soup = BeautifulSoup(r.text, "html.parser")
print(soup.prettify())
results = soup.find("ol",{"id": "b_results"})
links = results.findAll("li", {"class": "b_algo"})
