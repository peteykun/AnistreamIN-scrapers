import json
from bs4 import BeautifulSoup

anime = []
anime_links = []
boxart = []

with open('page.html', 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')

    for element in soup.find_all('h1', {"class": "tst-hover-title"}):
        anime.append(element.string)
    
    for element in soup.find_all('div', {"class": "av-grid-packshot"}):
        anime_links.append('https://www.primevideo.com' + element.contents[0]['href'].split('?')[0])
        boxart.append(element.contents[0].contents[0]['src'])

result = []

for i in range(len(anime)):
    try:
        print(anime[i])
        print(anime_links[i])
        print(boxart[i])
        print()

        result.append({
            'title': anime[i],
            'url': anime_links[i],
            'img_url': boxart[i]
        })
    except IndexError:
        print("{}/{}".format(i, len(boxart)))
        
print('')

print('{} anime found'.format(len(anime)))
print('{} anime links found'.format(len(anime_links)))
print('{} boxart images found'.format(len(boxart)))

with open('output.json', 'w') as f:
    json.dump(result, f)
