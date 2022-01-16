import pwd
from re import search
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import json
import os.path

def json_manager(data):
    if data == "check":
        if not os.path.isfile('CONFIG.json'):
            return False
    if data == "makefile":
        f = open('CONFIG.json', 'w')
        f.close()
    input_blog = str(input("티스토리 블로그 주소를 입력해주세요(https://포함) : "))
    g_id = str(input("서치콘솔 로그인에 사용될 구글 아이디를 입력하세요 : "))
    g_pw = str(input("서치콘솔 로그인에 사용될 구글 비밀번호를 입력하세요 : "))
    json_data = {
        "addr" : input_blog,
        "username" : g_id,
        "password" : g_pw
    }

def init():
    if os.path.isfile('CONFIG.json'):
        with open('CONFIG.json') as f:
            json_object = json.load(f)
    else:
        f = open('CONFIG.json', 'w')
        f.close()
        

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
    init()
    main()