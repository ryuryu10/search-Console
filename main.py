
from re import search
from tracemalloc import start
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from dist import config
from dist import printer
import json
import os


def json_manager(data):
    if data == "check":
        if not os.path.isfile('CONFIG.json'):
            return False

    if data == "makefile":
        f = open('CONFIG.json', 'w')
        f.close()

    if data == "edit":
        with open('CONFIG.json') as f:
            json_object = json.load(f)
        
    if data == "NEW_add":
        input_blog = str(input("티스토리 블로그 주소를 입력해주세요(https://포함) : "))
        g_id = str(input("서치콘솔 로그인에 사용될 구글 아이디를 입력하세요 : "))
        g_pw = str(input("서치콘솔 로그인에 사용될 구글 비밀번호를 입력하세요 : "))
        json_data = {
            "addr" : input_blog,
            "username" : g_id,
            "password" : g_pw
        }
        os.remove('CONFIG.json')
        with open('CONFIG.json', 'w') as f:
            json_string = json.dump(json_data, f, indent=2)


def main():
    if json_manager("check") == False:
        json_manager("makefile")
    printer.title()
    print("1. 블로그 링크 확인")
    print("2. Serach Console 확인")
    print("3. 설정값 확인 & 편집")
    input_data = input("번호를 입력하세요 : ")
    if input_data == "1":
        os.system('cls')
        print("확인할 페이지 범위를 입력하세요.")
        start_page = input("시작 페이지 : ")
        end_page = input("마지막 페이지 : ")
        scan_range = []
        for temp in range(int(start_page), int(end_page)+1):
            scan_range.append(temp)
        print(f"스캔할 범위는 : {scan_range}입니다")



def console():
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://store.leagueoflegends.co.kr/loot')
    driver.implicitly_wait(50)
    driver.quit()

while True:
    main()