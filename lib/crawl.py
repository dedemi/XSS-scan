import requests
from lib.log import Log
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

crawled_urls = []

def is_valid(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


def get_all_website_links(url):
    urls = set()
    domain_name = urlparse(url).netloc
    soup = BeautifulSoup(requests.get(url).content, "html.parser")

    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None:
            continue
        href = urljoin(url, href)
        parsed_href = urlparse(href)
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
        if not is_valid(href):
            continue
        if href in crawled_urls:
            continue
        if domain_name not in href:
            continue
        urls.add(href)
        Log.info(href)
        crawled_urls.append(href)
    return urls


def crawl(url, max_urls=50):
    global total_urls_visited
    total_urls_visited = 0
    urls = get_all_website_links(url)
    for link in urls:
        if total_urls_visited > max_urls:
            break
        total_urls_visited += 1
        urls.union(crawl(link, max_urls=max_urls))
    return urls