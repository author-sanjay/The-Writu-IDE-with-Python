from tkinter import *

compiler = Tk()
compiler.title("The Writu")

def run():
    print("Code Running")



menu_bar = Menu(compiler)
run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label="Run" , command=run)
menu_bar.add_cascade(label="Run", menu=run_bar)
compiler.config(menu=menu_bar)
editor = Text()
editor.pack()

compiler.mainloop()

