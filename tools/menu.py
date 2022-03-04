import keyboard
import os

from pandas import options

selection_range = 3
print_data = ['aaa','bbb','ccc']
selected = 0

def up():
    global selected
    if selected == 0:
        return
    selected -= 1
    show_menu()

def down():
    global selected
    if selected == selection_range-1:
        return
    selected += 1
    show_menu()

def exit():
    global selected
    print(selected)




def show_menu():
    global selected
    os.system('cls')
    print("Choose an option:")
    for i in range(0, selection_range):
        print("{1} {0} {3} {0} {2}".format(i, ">" if selected == i else " ", "<" if selected == i else " ", print_data[i]))

def data(input_title, input_options):
    global title, options
    title = input_title
    options = input_options

    show_menu()
    keyboard.add_hotkey('up', up)
    keyboard.add_hotkey('down', down)
    keyboard.add_hotkey('enter',exit)
    keyboard.wait()

menu(7,['a','b','c','d','e','f','g','h','i'])