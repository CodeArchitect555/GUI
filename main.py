import tkinter as tk
from tkinter import Label,Button,Entry 

class Main(tk.Frame):
    def __init__(self, master):
        self.myLabel = Label(master,text="todolist",width=10,height=5)
        self.myLabel.grid(row=0,column=0)
        options = {'padx':10, 'pady':10}
        self.entryBox = Entry(master)
        self.entryBox.grid(row=1,column=0)

        self.myButton =Button(master,text="enter task", command=self.clicker,**options)
        self.myButton.grid(row=2, column=0)
        
    def clicker(self):
        print("click")

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Todo app')
        self.geometry('175x150')

if __name__ == "__main__":
    app = App()
    Main(app)
    app.mainloop()