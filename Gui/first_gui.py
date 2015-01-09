import tkinter

class Application(tkinter.Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.bttn_quit = tkinter.Button (self, text="Quit")
        self.bttn_quit["command"] = self.quit
        self.bttn_quit.grid()

        self.bttn_hi = tkinter.Button(self, text="Hi")
        self.bttn_hi["command"] = self.say_hi
        self.bttn_hi.grid()

    def say_hi(self):
        print("Hello!")

root = tkinter.Tk()
root.title("Say hi!")
root.geometry("200x85")
app = Application(root)
root.mainloop()

