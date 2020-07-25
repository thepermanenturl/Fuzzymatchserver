import requests
import variable as v

r = requests.post("http://thepermanenturl.pythonanywhere.com/", json=v.d)
print(r.text)
