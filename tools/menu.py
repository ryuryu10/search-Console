import keyboard
import os

selection_range = 3
print_data = ['aaa','bbb','ccc']
selected = 0
func_active = True

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
        if selected == len(options)-1:
            return
        selected += 1
        show_menu()
    else:
        pass

def exit():
    global selected, func_active
    func_active = False
    print(selected)
    return selected
    

def show_menu():
    global title, options, selected
    os.system('clear')
    print("원하시는 작업을 선택하세요.")
    for a in range(0, len(options)):
        print('{1} [{0}] {3} {2}'.format(
            a,
            "-->" if selected == a else "   ",
            "<--" if selected == a else "   ",
            options[a]
            ))
    
def data(input_title, input_options):
    global title, options
    title = input_title
    options = input_options

    show_menu()
    keyboard.add_hotkey('up', up)
    keyboard.add_hotkey('down', down)
    keyboard.add_hotkey('enter',exit)
    keyboard.wait()

    return selected
