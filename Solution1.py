import requests
from bs4 import BeautifulSoup

url = input()
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

a = soup.select('div[class*=content-block] a')
my_points = []

for i in a:
    try:
        if i.text[0] == 'S' and len(i.text) > 1:
            my_points.append(i.text)
    except:
        continue
print(my_points[:-1])
