# Longevity
import tkinter

class Application(tkinter.Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.inst_lbl = tkinter.Label(self, text="Enter password for the secret of longevity")
        self.inst_lbl.grid(row=0, column=0, columnspan=2, sticky=tkinter.W)

        self.pw_lbl = tkinter.Label(self, text="Password: ")
        self.pw_lbl.grid(row=1, column=0, sticky=tkinter.W)
        self.pw_ent = tkinter.Entry(self)

        self.pw_ent.grid(row=1, column=1, sticky=tkinter.W)
        self.submit_bttn = tkinter.Button(self, text="Submit", command=self.reveal)

        self.submit_bttn.grid(row=2, column=0, sticky=tkinter.W)

        self.secret_txt = tkinter.Text(self, width=35, height=5, wrap=tkinter.WORD)
        self.secret_txt.grid(row=3, column=0, columnspan=2, sticky=tkinter.W)

    def reveal(self):
        contents = self.pw_ent.get()

        if contents == "secret":
            message = "Here's the secret living to 100: live to 99 and then be VERY careful"
        else:
            message = "That's not the correct pw, so I can't share the secret with you"

        self.secret_txt.delete(0.0, tkinter.END)
        self.secret_txt.insert(0.0, message)

root = tkinter.Tk()
root.title("Longevity")
root.geometry("300x150")

app = Application(root)
root.mainloop()