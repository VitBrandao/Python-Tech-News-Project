import requests
import time
from parsel import Selector
from tech_news.database import create_news


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
    news_information = dict()
    selector = Selector(text=html_content)

    # URL
    page_url = selector.css("link[rel*=canonical]::attr(href)").get()
    news_information['url'] = page_url

    # Título
    title = selector.css(".entry-title ::text").get()
    news_information['title'] = title.strip()

    # Data
    date = selector.css(".meta-date ::text").get()
    news_information['timestamp'] = date

    # Autor(a)
    writer = selector.css(".url.fn.n ::text").get()
    news_information['writer'] = writer

    # Comentários
    comments = selector.css("#comments .title-block ::text").get()
    if comments is None:
        comments = 0
    else:
        comments = comments[4:5]
    news_information['comments_count'] = comments

    # 1º Parágrafo
    summary = selector.xpath("string(.//div[@class='entry-content']/p)").get()
    if summary is None:
        summary = []

    news_information['summary'] = summary.strip()

    # Tags
    get_page_tags = selector.css(".post-tags a::text").getall()
    if get_page_tags is not None:
        tags = get_page_tags
    else:
        tags = []

    news_information['tags'] = tags

    # Categoria
    category = selector.css(".category-style .label ::text").get()
    news_information['category'] = category

    return news_information


# Requisito 5
def get_tech_news(amount):
    trybe_url = "https://blog.betrybe.com"

    all_news = []
    for _ in range(amount):
        links = scrape_novidades(fetch(trybe_url))
        for link in links:
            all_news.append(link)

        trybe_url = scrape_next_page_link(fetch(trybe_url))
    all_news = all_news[:amount]
    # print(all_news)

    tech_news = []
    for news in all_news:
        news_object = scrape_noticia(fetch(news))
        tech_news.append(news_object)
    # print(tech_news)

    create_news(tech_news)

    return tech_news


# get_tech_news(3)
