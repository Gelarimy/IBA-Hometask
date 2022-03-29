from bs4 import BeautifulSoup
from get_pages import *

def get_news_links(page):
    soup = BeautifulSoup(page, "html.parser")
    data = soup.find_all("a", class_="news-link")

    news_links = []

    for link in data:
        news_links.append("https://visa.vfsglobal.com{}".format(link.get("href")))

    return news_links


def get_date_and_news(page):
    soup = BeautifulSoup(page, "html.parser")
    raw_date = soup.find("h5", class_="news-date")
    date = str(raw_date.string)
    raw_news = soup.find("div", class_="v-content__wrap")
    news = raw_news.find('div', class_="renderer-content")

    new = []

    for string in news.strings:
        new.append(string)

    return date, new


def get_news():
    url = "https://visa.vfsglobal.com/blr/ru/nor"
    driver_sel = create_driver()
    main_page = get_page(driver_sel, url)
    news_links = get_news_links(main_page)

    data = []
    for link in news_links:
        page = get_page(driver_sel, link)
        date, news = get_date_and_news(page)
        data.append({"date": date, "news": news})
    close_driver(driver_sel)
    return data
