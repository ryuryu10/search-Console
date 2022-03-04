import keyboard
import os

from sqlalchemy import func
from function import temper

print_menus = ['대기','환경설정']

selected = 0
func_active = True

def show_menu():
    global selected
    os.system('cls')
    print("진행할 작업을 선택하세요.")
    print("-"*30)
    for i in range(0, len(print_menus)):
        print("{1} [{0}]  {3} {2}".format(i, "-->" if selected == i else "   ", "<--" if selected == i else "  ",print_menus[i]))
    print("-"*30)
    print("↑ ↓ : 메뉴 선택 | ↵ : 선택된 메뉴 실행")

def up():
    if func_active == True:
        global selected
        if selected == 0:
            return
        selected -= 1
        show_menu()
    else:
        pass

def down():
    if func_active == True:
        global selected
        if selected == len(print_menus)-1:
            return
        selected += 1
        show_menu()
    else:
        pass

def enter():
    global selected, func_active
    func_active = False
    if selected == 0:
        pass
    elif selected == 1:
        temper.aaaa()
    elif selected == 2:
        pass
    
    print(selected)
    
show_menu()
keyboard.add_hotkey('up', up)
keyboard.add_hotkey('down', down)
keyboard.add_hotkey('enter', enter)
keyboard.wait()