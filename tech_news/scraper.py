import requests
import time

# trybe_url = "https://blog.betrybe.com"


# Requisito 1
def fetch(url):
    try:
        response = requests.get(
            url,
            headers={"user-agent": "Fake user-agent"},
            timeout=3
        )
        time.sleep(1)
    except requests.ReadTimeout:
        return None

    finally:
        if(response.status_code != 200):
            return None

        return response.text


# fetch(trybe_url)


# # Requisito 2
# def scrape_novidades(html_content):
#     """Seu código deve vir aqui"""


# # Requisito 3
# def scrape_next_page_link(html_content):
#     """Seu código deve vir aqui"""


# # Requisito 4
# def scrape_noticia(html_content):
#     """Seu código deve vir aqui"""


# # Requisito 5
# def get_tech_news(amount):
#     """Seu código deve vir aqui"""
