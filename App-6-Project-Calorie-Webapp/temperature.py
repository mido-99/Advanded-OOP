import requests
from selectorlib import Extractor

class Temperature:
    '''Get the current temperature of a city'''
    
    def __init__(self, country, city):
        self.country = country
        self.city = city
        
    def get(self):
        
        city = self.city.strip().replace(' ', '-').lower()
        country = self.country.strip().replace(' ', '-').lower()
        
        r = requests.get(f"https://www.timeanddate.com/worldclock/{country}/{city}")
        cont = r.text
        
        ext = Extractor.from_yaml_file("temp.yaml")
        data = ext.extract(cont)
        temp = int(data['temp'][:-2])
        
        return temp

if __name__ == "__main__":
    tem = Temperature("Cote dIvoire ", 'Bouake')
    print(tem.get())