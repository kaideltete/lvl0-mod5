"""
Write an algorithm to change a string into a "goofy" version.
"""
import random
from tkinter import messagebox, simpledialog, Tk
window=Tk()

if __name__ == '__main__':
    # TODO)
    #  1. Ask the user to enter their name.
    #  2. Use a loop to alternately modify each character of the name into
    #     uppercase and lowercase letters until a new "goofy" representation
    #     of their name has been constructed.
    #     For example, if they enter their name as Alexander Hamilton
    #     their goofy name will be AlExAnDeR HaMiLtOn
    #  3. Show the user the goofy version of their name in a pop-up.

    name1 = simpledialog.askstring(title='1?', prompt="what is your name")

    name2=""

    for i in range(len(name1)):
        var=random.randint(0, 1)
        if var == 1:
            name2=name2+name1[i:i+1].lower()
        if var == 0:
            name2=name2+name1[i:i+1].upper()


    messagebox.showinfo(message="here is your changed name,"+str(name2)+".")
    pass
