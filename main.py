from re import search
from tracemalloc import start
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from dist import config
from dist import printer
from function import scanner
import json
import os

def json_manager(data):
    if data == "check":
        if not os.path.isfile('CONFIG.json'):
            return False

    if data == "makefile":
        pass

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
            link = json_string["addr"]

def main():
    print("구글 서치 콘솔 간편 도구")
    print("원하시는 기능을 선택해 주세요.")
        
        

while True:
    main()