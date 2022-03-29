from selenium import webdriver
import time

global driver


def create_driver():
    EXE_PATH = r"C:\chrome_driver\chromedriver.exe"
    return webdriver.Chrome(executable_path=EXE_PATH)


def get_page(driver, url):
    driver.get(url=url)
    time.sleep(2)
    html = driver.page_source
    return html


def close_driver(driver):
    driver.close()
    driver.quit()
