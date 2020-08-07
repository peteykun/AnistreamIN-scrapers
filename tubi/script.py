import json
from bs4 import BeautifulSoup

anime = []
anime_links = []
boxart = []

with open('page.html', 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')

    for element in soup.find_all('div', {"class": "Col Col--4 Col--lg-3 Col--xl-1-5 Col--xxl-2"}):
        for subElement in element.findChildren('a', {"class": 'ATag'}):
            if(subElement['href']).startswith('/series') or (subElement['href']).startswith('/movies'):
                anime.append(subElement.contents[0])
                anime_links.append('http://www.tubitv.com' + subElement['href'])
                boxart.append('http://' + str(element.contents[0]).split('//')[-1].split('"')[0])

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
