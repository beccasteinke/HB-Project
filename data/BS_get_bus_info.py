import requests
from bs4 import BeautifulSoup
import lxml
from pprint import pprint
import sys

# orig_stdout = sys.stdout
# f = open('full_data.json', 'w')
# sys.stdout = f

url_list = ['https://wellconnectedtwincities.com/business/village-health-llc/',
 'https://wellconnectedtwincities.com/business/statera-health/',
 'https://wellconnectedtwincities.com/business/bethany-hansen/',
 'https://wellconnectedtwincities.com/business/christine-lord-licsw-sep/',
 'https://wellconnectedtwincities.com/business/radiant-source-wellness/',
 'https://wellconnectedtwincities.com/business/caty-brown/']

print(type(url_list))

urls_info = []
links = []

for link in url_list:
    r = requests.get(link)
    src = r.content
    soup = BeautifulSoup(src, 'lxml')

    for div in soup.find_all("div", {"class": "fl-widget"}):
        for link in div.select("a"):
            # links.append(link)
            links.append(link['href'])

pprint(links)


# urls_info.append({'URL': (links[1])})
# urls_info.append({'Facebook': (links[2])})
# urls_info.append({'Instagram': (links[3])})
# urls_info.append({'Tel': (links[4][4:])})

# pprint(urls_info)


# with open('full_data.json', 'wt') as out:
#     pprint(urls_info, stream=out)

# sys.stdout = orig_stdout
# f.close()

# [1] = URL
# [2] = Facebook
# [3] = Instagram
# [4] = tel