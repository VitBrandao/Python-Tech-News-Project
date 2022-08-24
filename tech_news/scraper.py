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


# response = requests.get(
#     'https://blog.betrybe.com/carreira/livros-sobre-lideranca/',
#     headers={"user-agent": "Fake user-agent"},
# )

# print(scrape_noticia(response.text))


# Requisito 5
def get_tech_news(amount):
    return 0
