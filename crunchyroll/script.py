import json
from bs4 import BeautifulSoup

anime = []
anime_links = []
boxart = []

with open('page.html', 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')

    for element in soup.find_all('a', {"class": "portrait-element"}):
        anime.append(element.contents[3].string)
        anime_links.append('https://www.crunchyroll.com' + element['href'])
        boxart.append(element.contents[1].contents[0]['src'])

result = []

for i in range(len(anime)):
    print(anime[i])
    print(anime_links[i])
    print(boxart[i])
    print()

    result.append({
        'title': anime[i],
        'url': anime_links[i],
        'img_url': boxart[i],
        'paid': False
    })

print('{} anime found'.format(len(anime)))

with open('output.json', 'w') as f:
    json.dump(result, f, indent=4)
