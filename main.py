# main menu for mass config python project
from tkinter import *
from tkinter import ttk


def main():
    #print menu
    # print("1) Push Stock Configuration")
    # print("2) Push Custom Configurations")
    # print("3) Exit")
    # option = input();
    # print(option)
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
    root.mainloop()
    input("Press enter to exit ;)")

main()