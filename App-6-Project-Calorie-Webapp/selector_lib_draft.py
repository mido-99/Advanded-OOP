import requests
from selectorlib import Extractor

r = requests.get("https://www.timeanddate.com/worldclock/usa/new-york")

cont = r.text

# Extract data from request text
ext = Extractor.from_yaml_file("temp.yaml")

data = ext.extract(cont)
temp = data['temp'][:-2]

print(temp)