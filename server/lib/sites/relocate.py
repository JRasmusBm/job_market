from bs4 import BeautifulSoup
from models.Offer import Offer
import grequests

relocate = {
    "url": "https://relocate.me",
    "search": "/search/software/the-netherlands?time=any",
    "href": "/the-netherlands/",
}


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


async def extract_location(soup):
    country_tag = soup.select(".job-info__country")[0]
    country_tag.img.extract()
    return "".join(country_tag.contents).strip()


async def extract_company(soup):
    company_tag = soup.select(".job-info__company")[0]
    company_tag.img.extract()
    return "".join(company_tag.contents).strip()


async def extract_job(response):
    soup = BeautifulSoup(response.content, "html.parser")
    return Offer(
        title=await extract_title(soup),
        company=await extract_company(soup),
        location=await extract_location(soup),
        link=response.url,
    )


async def jobs():
    relocate_me_links = await job_links(relocate)
    return [
        await extract_job(res)
        for res in grequests.map(grequests.get(link) for link in relocate_me_links)
    ]
