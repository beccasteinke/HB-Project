import requests
from bs4 import BeautifulSoup
import lxml
from pprint import pprint
import sys

################ This is my attempt at trying to read a file to get all of the data
# orig_stdout = sys.stdout
# f = open('full_data.json', 'w')
# sys.stdout = f

# f = open('data.xml', 'r')
# url_str = f.read()
# print(url_str)
# url_list = url_str.split(", ")
# print(url_list)
################


urls_info = []
links = []


for link in range(len(url_list)):
    r = requests.get(link)
    src = r.content
    soup = BeautifulSoup(src, 'lxml')    

    for div in soup.find_all("div", {"class": "fl-widget"}):
        for link in div.select("a"):
            # links.append(link)
            links.append(link['href'])
# print(links)

urls_info.append({'URL': (links[1])})
urls_info.append({'Facebook': (links[2])})
urls_info.append({'Instagram': (links[3])})
urls_info.append({'Tel': (links[4][4:])})

pprint(urls_info)

# Print info to a new json file
# with open('full_data.json', 'wt') as out:
#     pprint(urls_info, stream=out)







# sys.stdout = orig_stdout
# f.close()

# [1] = URL
# [2] = Facebook
# [3] = Instagram
# [4] = tel