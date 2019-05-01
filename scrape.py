from bs4 import BeautifulSoup
from pprint import pprint
from dataclasses import dataclass
import grequests
import asyncio

relocate = {
    "url": "https://relocate.me",
    "search": "/search/software/the-netherlands?time=any",
    "href": "/the-netherlands/",
}


@dataclass
class Offer:
    title: str
    company: str

    def __str__(self):
        return f"""
            Title: {self.title}
            Company: {self.company}
            """


async def job_links(site):
    base_url = site.get("url", "") + site.get("search", "")
    response = grequests.map([grequests.get(base_url, timeout=5)])[0]
    soup = BeautifulSoup(response.content, "html.parser")
    links = [
        site.get("url", "") + link.get("href")
        for link in soup.find_all("a")
        if site.get("href", "") in link.get("href")
    ]
    return links


async def extract_title(soup):
    return "".join(soup.select(".job-info__heading h1")[0].contents).strip()


async def extract_company(soup):
    company_tag = soup.select(".job-info__country")[0]
    company_tag.img.extract()
    return "".join(company_tag.contents).strip()


async def extract_job(response):
    soup = BeautifulSoup(response.content, "html.parser")
    offer = Offer(title=await extract_title(soup), company=await extract_company(soup))
    print(offer)


async def jobs():
    relocate_me_links = await job_links(relocate)
    pprint(relocate_me_links)
    return [
        await extract_job(job)
        for job in grequests.map(grequests.get(link) for link in relocate_me_links)
    ]


print(asyncio.run(jobs()))
