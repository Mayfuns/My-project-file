# import random
import random
from tkinter import *
from tkinter.ttk import *

def generate_password():
    entry.delete(0, END)
    password_chars = ""
    password_len = 15
    
    for char in range(33, 127):
        password_chars += chr(char)
 
    password = "" 
    for i in range(password_len):
        character = random.choice(password_chars)
        password += character
        
    return password


def generate():
    password = generate_password()
    entry.insert(10, password)
    
# initialize tkinter
root = Tk()
root.title("Password Generator")

label = Label(root, text = "My Password")
label.grid(row = 0)
entry = Entry(root)
entry.grid(row=0, column=1)

password_button = Button(root, text="Generate", command=generate)
password_button.grid(row=0, column = 3)





root.mainloop()
