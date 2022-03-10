from cgi import test
from re import search
from tracemalloc import start
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import requests

def start(link, pages):
    driver=webdriver.Chrome(ChromeDriverManager().install())
    for count in pages:
        link = f'{link}/{count}'
    driver.get(link)
    driver.implicitly_wait(50)
    driver.quit()

def Connection(test_url):
    try:
        r = requests.get(test_url)
        return r.status_code
    except:
        return 000