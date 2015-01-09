# Lazy Buttons 2

import tkinter

class Application(tkinter.Frame):

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.bttn1 = tkinter.Button(self, text="I do nothing")
        self.bttn1.grid()

        self.bttn2 = tkinter.Button(self)
        self.bttn2.grid()
        self.bttn2.configure(text="Me too!")

        self.bttn3 = tkinter.Button(self)
        self.bttn3.grid()
        self.bttn3["text"] = "Same here!"

root = tkinter.Tk()
root.title("Lazy Buttons 2")
root.geometry("200x85")

app = Application(root)

root.mainloop()