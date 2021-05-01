import requests

from bs4 import BeautifulSoup

link = input()
r = requests.get(link)
soup = BeautifulSoup(r.content, 'html.parser')
a = soup.find_all('a')
out = []
for i in a:
    if len(i.text) > 1 and i.text[0] == 'S' and ('topic' in i.get('href') or 'entity' in i.get('href')):
        # print(i.get('href'), i.text)
        out.append(i.text)
print(out)
