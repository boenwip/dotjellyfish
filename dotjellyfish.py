import os
import random
import string
from datetime import datetime
from tkinter import *
import sys

# Set Desired Location of _hidden_ password file
os.chdir('/Documents/.jellyfish.md')
if True:
    print(os.getcwd())

# Get the current date and time
now = datetime.now()
today = str(now.strftime('%Y-%m-%d %H:%M:%S'))


# Function to create the password
### - Create password with pw
### - Print Output 
### - Print output with current date time
def password_generator():
    password = string.ascii_letters + string.digits
    pw = "".join(random.choice(password) for x in range(random.randint(12, 15)))
    print('#' * 30)
    print(str(src.get()) + ' ' + today)
    return pw


# Function for output to password to file
def write_pw():
    f = open('.jellyfish.md', 'a')
    sys.stdout = f
    print('')
    print(str(password_generator()))
    f.close()


# Make the GUI
rootWindow = Tk()
rootWindow.geometry('500x150')
rootWindow.title("Password Generator")

# GUI What is the password for? Statement and Entry Box
p = Label(rootWindow, text="What's the password for?")
p.config(font=('Default', 16))
p.place(anchor=CENTER,
        x=250,
        y=40,
        )

src = Entry(rootWindow)
src.place(anchor=CENTER,
          x=250,
          y=75,
          )

# GUI generate button
generate = Button(rootWindow,
                  text="Generate",
                  command=write_pw,
                  activeforeground='blue',
                  height=2,
                  width=10,
                  font=('Default', 16),
                  )

generate.place(anchor=CENTER,
               x=250,
               y=110,
               )

# While loop for running window
rootWindow.mainloop()
