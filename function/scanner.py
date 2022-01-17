from re import search
from tracemalloc import start
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

def start(link, pages):
    driver=webdriver.Chrome(ChromeDriverManager().install())
    for count in pages:
        link = f'{link}/{count}'
    driver.get(link)
    driver.implicitly_wait(50)
    driver.quit()