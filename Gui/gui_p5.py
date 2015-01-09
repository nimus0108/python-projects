# Movie Chooser

import tkinter

class Application(tkinter.Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        tkinter.Label(self, text="Choose your favorite movie types").grid(row=0, column=0, sticky=tkinter.W)
        tkinter.Label(self, text="Select all that apply").grid(row=0, column=0, sticky=tkinter.W)
        tkinter.Label(self, text="Select all that apply: ").grid(row=1, column=0, sticky=tkinter.W)

        self.likes_comedy = tkinter.BooleanVar()
        tkinter.Checkbutton(self, text="Comedy", variable=self.likes_comedy, command=self.update_text()).grid(row=2, column=0, sticky=tkinter.W)

        self.likes_drama = tkinter.BooleanVar()
        tkinter.Checkbutton(self, text="Drama", variable=self.likes_drama, command=self.update_text()).grid(row=3, column=0, sticky=tkinter.W)

        self.likes_romance = tkinter.BooleanVar()
        tkinter.Checkbutton(self, text="Romance", variable=self.likes_romance, command=self.update_text()).grid(row=4, column=0, sticky=tkinter.W)

        self.results_txt = tkinter.Text(self, width=40, height=5, wrap=tkinter.WORD)
        self.results_txt.grid(row=5, column=0, columnspan=3)

    def update_text(self):
        likes = ""
        if self.likes_comedy.get():
            likes += "You like comedic movies. \n"
        if self.likes_drama.get():
            likes += "You like dramatic movies. \n"
        if self.likes_romance.get():
            likes += "You like romantic movies. \n"

        self.results_txt.delete(0.0, tkinter.END)
        self.results_txt.insert(0.0, tkinter.LIKES)

root = tkinter.Tk()
root.title("Movie Chooser")
app = Application(root)
root.mainloop()