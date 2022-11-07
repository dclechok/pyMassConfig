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
    options = [
        "Push Stock Configuration", 
        "Push Custom Configuration"
    ]
    var="Test"
    gui = Tk(className='Mawson Network Mass Config Tool')
# set window size
    gui.geometry("700x500")
    gui.resizable(False, False)
    frame = ttk.Frame(gui)
    Label(gui, text = "Password").place(x = 40, y = 100)
    Label(gui, text = "C")
    option = StringVar(value="Select an option")
    OptionMenu(gui, option, *options ).place(x = 170, y = 80)
    gui.mainloop() 

main()