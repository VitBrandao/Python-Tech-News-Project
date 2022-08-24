from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    news_in_db = search_news({"title": {"$regex": title, "$options": "i"}})
    news_list = list()

    for news in news_in_db:
        news_list.append((news['title'], news['url']))

    return news_list


# Requisito 7
def search_by_date(date):
    news_by_date = list()

    try:
        format_date = datetime.strptime(date, '%Y-%m-%d')

        date_timestamp = datetime.strftime(format_date, '%d/%m/%Y')

        news_in_db = search_news({'timestamp': date_timestamp})
        for news in news_in_db:
            news_by_date.append((news['title'], news['url']))

    except ValueError:
        raise ValueError('Data inválida')

    return news_by_date


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
