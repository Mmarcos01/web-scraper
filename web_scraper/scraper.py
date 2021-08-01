import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'
page = requests.get(URL)

def get_citations_needed_count(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    citations = soup.find_all(class_= 'Template-Fact')
    print (len(citations))


def get_citations_needed_report(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    citations = soup.find_all(class_= 'Template-Fact')
    for cite in citations:
        print(cite.parent.text)

get_citations_needed_count(URL)
get_citations_needed_report(URL)
