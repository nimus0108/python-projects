# Lazy Buttons

import tkinter

root = tkinter.Tk()
root.title("Lazy Buttons")
root.geometry("200x85")

app = tkinter.Frame(root)
app.grid()

bttn1 = tkinter.Button(app, text="I do nothing!")
bttn1.grid()

bttn2 = tkinter.Button(app)
bttn2.configure(text="Me too!")
bttn2.grid()

bttn3 = tkinter.Button(app)
bttn3.grid()
bttn3["text"] = "Same here!"

root.mainloop()