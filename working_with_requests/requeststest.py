import requests

r = requests.get("http://www.google.com")
print("STATUS:", r.status_code)
print(r.text)
f = open("./page.html", "w+")
f.write(r.text)
f.close()
