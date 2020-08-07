import json
from bs4 import BeautifulSoup

anime = []
anime_links = []
boxart = []

with open('page.html', 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')

    for element in soup.find_all('p', {"class": "fallback-text"}):
        anime.append(element.string)
        
    for element in soup.find_all('a', {"class": "slider-refocus"}):
        anime_links.append('https://www.netflix.com/' + element['href'].split('?')[0])
    
    for element in soup.find_all('img', {"class": "boxart-image"}):
        boxart.append(element['src'])

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
