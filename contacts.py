from get_pages import *
from bs4 import BeautifulSoup


def get_contacts():
    contacts = {
        "visa_center": get_page_contacts()
    }
    return contacts


def get_page_contacts():
    url = "https://visa.vfsglobal.com/blr/ru/nor/attend-centre/Minsk"
    driver_sel = create_driver()
    page = get_page(driver_sel, url)
    inf = main_contacts(page)

    return inf


def main_contacts(page):
    map_res = {}
    soup = BeautifulSoup(page, 'html.parser')

    a1 = soup.find('div', class_='font-size18')
    a2 = a1.find('div', class_='renderer-content')

    map_res['Adress'] = a2.string

    l_temp = []

    for i in soup.findAll('td', class_='attend-center-td'):
        l_temp.append(i.getText())

    map_res['Schedule'] = l_temp

    return map_res
