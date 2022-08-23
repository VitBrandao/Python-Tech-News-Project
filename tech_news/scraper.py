import requests
import time
from parsel import Selector

trybe_url = "https://blog.betrybe.com"


# Requisito 1
def fetch(url):
    try:
        response = requests.get(
            url,
            headers={"user-agent": "Fake user-agent"},
            timeout=3
        )
        time.sleep(1)

        if(response.status_code != 200):
            return None

        return response.text

    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)

    class_p1 = ".cs-overlay.cs-overlay-hover"
    class_p2 = ".cs-bg-dark.cs-overlay-ratio.cs-ratio-landscape "
    a_attr = "a::attr(href)"
    class_name = class_p1 + class_p2 + a_attr

    all_news_url = selector.css(class_name).getall()

    if len(all_news_url) == 0:
        return []

    return all_news_url


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_url = selector.css(".next.page-numbers ::attr(href)").get()

    if next_page_url:
        return next_page_url
    else:
        return None


# Requisito 4
def scrape_noticia(html_content):
    return 0


# Requisito 5
def get_tech_news(amount):
    return 0
