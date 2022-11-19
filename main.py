from tkinter import *

root = Tk()
root.title('todo list')
root.geometry()

class Elder:
    def __init__(self, master):
        myFrame = Frame(master)
        myFrame.grid()

        self.myLabel = Label(master,text="todolist",width=10,height=5)
        self.myLabel.grid(row=0,column=0)

        self.entryBox = Entry(master)
        self.entryBox.grid(row=1,column=0)

        self.myButton =Button(master,text="enter task", command=self.clicker)
        self.myButton.grid(row=2, column=0)
        
    def clicker(self):
        print("look at you your clicky")


e = Elder(root)

root.mainloop()