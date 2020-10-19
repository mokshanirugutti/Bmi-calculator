from math import *
from tkinter import *
from tkinter import messagebox

# Universal Properties
universal_font = ('Arial', 10, 'bold')
head_font =("Arial",20,'bold')

# Initialise Root i.e Window
root = Tk()
title = Label(root, text="BMI calclulator ", font=head_font)
title.grid(row=0, column=0,pady=25,ipadx=25)
# Labels Are Here
weight_label = Label(root, text="Weight in kilograms : ", font=universal_font, )
weight_label.grid(row=1, column=0,ipadx=10)

height_label = Label(root, text="Height in foot : ", font=universal_font)
height_label.grid(row=2, column=0)


def calculate_bmi():
    # Lets get the values from each entry
    wght = weight.get()
    hght = height.get()
    # Notes: BMI - Formula = (weight / height ^ 2)
    height_ms = hght*12/39.37
    bmi = wght /pow(height_ms, 2)  # We'r converting it to metre..
    if bmi >25:
    	messagebox.showwarning("Results", "OverWeight")
    elif bmi<18:
    	messagebox.showwarning("Results", "UnderWeight")
    else:
    	messagebox.showinfo("Results", "you are Fit")
    	


# We need Height And Weight Entries
# Text Variables are here...
global weight
global height

weight = IntVar()
height = IntVar()

weight_entry = Entry(root, textvariable=weight, width=20,fg = "white", bg = "black",
                     bd=3, font=universal_font)

weight_entry.grid(row=1, column=1)


height_entry = Entry(root, textvariable=height, width=20,fg = "white", bg = "black",
                     bd=3, font=universal_font)

height_entry.grid(row=2, column=1)

# Now We need A Button...
btn_calculate = Button(root, width=5, text="Calculate",
                       font=universal_font, bd=3, command=calculate_bmi)
btn_calculate.grid(row=3, columnspan=3, pady=50)

# Root Window Configurations...
root.title("BMI Calculator")
root.resizable(False, False)
root.mainloop()
