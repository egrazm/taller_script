import requests

city = "Asunción"
r = requests.get(f"https://wttr.in/{city}?format=3")
print("Clima actual:", r.text)
