import tkinter as tk
from tkinter import Label,Button,Entry 

class Main(tk.Frame):
    def __init__(self, master):
        self.myLabel = Label(master,text="Enter todo item:")
        self.myLabel.grid(row=0,column=0)
        options = {'padx':10, 'pady':10}
        self.entryBox = Entry(master)
        self.entryBox.grid(row=1,column=0,columnspan=3)

        self.myButton =Button(master,text="enter task", command=self.clicker,**options)
        self.myButton.grid(row=2, column=0)
        
        self.myButton2 =Button(master,text="enter task", command=self.clicker,**options)
        self.myButton2.grid(row=2, column=1)
        
        self.myButton3 =Button(master,text="enter task", command=self.clicker,**options)
        self.myButton3.grid(row=2, column=2)
        

    def clicker(self):
        print("click")

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Todo app')
        self.geometry('300x300')

if __name__ == "__main__":
    app = App()                 
    Main(app)
    app.mainloop()