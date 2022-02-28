import time
import keyboard 
import mouse

isClicking = False

def set_clicker():
    global isClicking
    if isClicking:
        isClicking = False
        print('off')
    
    else:
        isClicking = True
        print("on")

activkey = input('Choose 2 keys ("alt+z" for example): ')

whatbutton = input('What button? Left or Right?: ')

keyboard.add_hotkey(activkey, set_clicker)

while True:
    if isClicking:
        mouse.double_click(button = whatbutton)
        time.sleep(0.01)

