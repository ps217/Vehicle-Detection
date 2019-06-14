# import module from tkinter for UI
from tkinter import *
import os
from datetime import datetime;

# creating instance of TK
root = Tk()

root.configure(background="white")


def function1():
    os.system("python car.py")


def function2():
    os.system("python two_wheeler.py")


def function3():
    os.system("python pedestrian.py")


def function4():
    os.system("python bus.py")


def function6():
    root.destroy()


# stting title for the window

root.title("Vehicle Finder")

# creating a text label
Label(root, text="Vehicle and Pedestrian Detection", font=("times new roman", 20), fg="white", bg="black",
      height=3).grid(row=0, rowspan=2, columnspan=2, sticky=N + E + W + S, padx=5, pady=5)

# creating first button
Button(root, text="CAR DETECTION", font=("times new roman", 20), bg="#000000", fg='green', command=function1).grid(
    row=4, columnspan=2, sticky=W + E + N + S, padx=5, pady=5)

# creating second button
Button(root, text="TWO WHEELER DETECTION", font=("times new roman", 20), bg="#000000", fg='green',
       command=function2).grid(row=5, columnspan=2, sticky=N + E + W + S, padx=5, pady=5)

# creating third button
Button(root, text="PEDESTRIAN DETECTION", font=('times new roman', 20), bg="#000000", fg="green",
       command=function3).grid(row=6, columnspan=2, sticky=N + E + W + S, padx=5, pady=5)

Button(root, text="BUS DETECTION", font=('times new roman', 20), bg="#000000", fg="green", command=function4).grid(
    row=7, columnspan=2, sticky=N + E + W + S, padx=5, pady=5)

Button(root, text="EXIT", font=('times new roman', 20), bg="black", fg="red", command=function6).grid(row=9,
                                                                                                      columnspan=2,
                                                                                                      sticky=N + E + W + S,
                                                                                                      padx=5, pady=5)

root.mainloop()
