from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import json

def init():
    pass
    pass
def main():
    print("1. 404 체커")
    print("2. console 확인")
    print("><><><><><><><><><><><")
    input_data = input("NUMBER --> ")
    if input_data == "1":
        console()

def console():
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://store.leagueoflegends.co.kr/loot')
    driver.implicitly_wait(50)
    driver.quit()

while True:
    main()