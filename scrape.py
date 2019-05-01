from bs4 import BeautifulSoup
from pprint import pprint
import requests

sites = {
    "relocate": {
        "url": "https://relocate.me/search/software/the-netherlands?time=any",
        "href": "/the-netherlands/",
    }
}


def scrape(site):
    base_url = site.get("url", "")
    response = requests.get(base_url, timeout=5)
    content = BeautifulSoup(response.content, "html.parser")
    links = [
        link.get("href")
        for link in content.find_all("a")
        if site.get("href", "") in link.get("href")
    ]
    pprint(links)


for site in sites:
    scrape(sites[site])
