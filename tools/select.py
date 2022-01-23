import keyboard
import os

NUMBER = 1

def output():
    os.system('cls')
    global NUMBER
    print("Choose an option:")

    for i in range(1, 5):
        print("{1} {0}. Do something {0} {2}".format(i, ">" if selected == i else " ", "<" if selected == i else " "))

def up():
    global selected
    if selected == 1:
        return
    selected -= 1
    show_menu()

def down():
    global selected
    if selected == 4:
        return
    selected += 1
    show_menu()

def menu(number, data):
    output()
    keyboard.add_hotkey('up', up)
    keyboard.add_hotkey('down', down)
    keyboard.wait()