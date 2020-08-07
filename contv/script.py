import json
from bs4 import BeautifulSoup

anime = []
anime_links = []
boxart = []

with open('page.html', 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')

    for element in soup.find_all('p', {"class": "asset-bottom-title"}):
        anime.append(element.string)
        
    for element in soup.find_all('div', {"class": "jtvt-cat-humbnail"}):
        anime_links.append('https://www.contv.com' + element.contents[0]['href'].split('?')[0])
        boxart.append(element.contents[0].contents[0].contents[2].contents[0].contents[0]['src'])

result = []

for i in range(len(anime)):
    print(anime[i])
    print(anime_links[i])
    print(boxart[i])
    print()

    result.append({
        'title': anime[i],
        'url': anime_links[i],
        'img_url': boxart[i]
    })

print()

print('{} anime found'.format(len(anime)))
print('{} anime links found'.format(len(anime_links)))
print('{} boxart images found'.format(len(boxart)))

with open('output.json', 'w') as f:
    json.dump(result, f)
