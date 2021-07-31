import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'
page = requests.get(URL)

# print(page)
# print(page.__dir__())

soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)

# sup class="noprint Inline-Template Template-Fact"
# results = soup.find(class_= '"Wikipedia:Citation needed"')
citations = soup.find_all(class_= 'Template-Fact')
print(citations)
print(len(citations))

def get_citations_needed_count(URL):
    citations = soup.find_all(class_= 'Template-Fact')
    print(len(citations))

def get_citations_needed_report():
