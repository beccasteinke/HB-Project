# Beautiful Soup Play

import requests
from bs4 import BeautifulSoup
import lxml
import pprint

# Create beautiful soup object with results from page 1
result = requests.get("https://wellconnectedtwincities.com/directory/")
src = result.content
soup = BeautifulSoup(src, 'lxml')

urls_for_data = []
urls_info = []

for a_tag in soup.find_all("a", "pp-content-grid-more pp-more-link-button"):
    urls_for_data.append(a_tag.attrs['href'])

print(urls_for_data)

# pprint.pprint(list(soup.children))

# for item in range(len(urls)):
#     orgs = requests.get([urls])
#     orgs_src = orgs.content
#     orgs_soup = BeautifulSoup(orgs_src, 'lxml')

#     for a_tag in orgs_soup.find_all("a"):
#         url_info.append(a_tag.attrs['href'])

#     pprint.pprint(url_info)






"""I need to loop thru each url and get <a> tags with titles facebook, instagram, website"""   

# soupfinal = BeautifulSoup(urls, 'lxml')
# for url_a_tags in urls:
#     soupfinal.find_all("a")
#     urls_info.append(url_a_tag.attrs['href'])

# print(urls_info)

    # for i in range(len(urls)):
    #     """Iterate over each url"""
    #     for a_tags in soup1.find_all("a"):
    #         urls_info.append(a_tag.attrs['href'])

# print(urls_info)

