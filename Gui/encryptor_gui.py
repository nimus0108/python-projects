import tkinter
from Gui.Encryptor import Encryptor
e = Encryptor("cipher1.txt")

class Application(tkinter.Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        tkinter.Label(self,
              text = "Enter the message:"
              ).grid(row = 0, column = 0, columnspan = 2, sticky = tkinter.W)

        self.msg = tkinter.Text(self, width=35, height=5, wrap = tkinter.WORD)
        self.msg.grid(row = 2, column = 0, columnspan = 2,  sticky = tkinter.W)

        # Buttons
        tkinter.Button(self,
               text = "Encrypt",
               command = self.encrypt
               ).grid(row = 3, column = 0, sticky = tkinter.W)

        tkinter.Button(self,
               text = "Decrypt",
               command = self.decrypt
               ).grid(row = 3, column = 1, sticky = tkinter.W)


        # "Out"
        tkinter.Label(self,
              text = "Out:"
              ).grid(row = 4, column = 0, columnspan = 2, sticky = tkinter.W)

        #Output
        self.msg_text = tkinter.Text(self, width=35, height=5, wrap = tkinter.WORD)
        self.msg_text.grid(row = 5, column = 0, columnspan = 2, sticky = tkinter.W)


    def encrypt(self):
        message = self.msg.get(0.0, tkinter.END)
        encrypted = e.encrypt_message(message)

        self.msg_text.delete(0.0, tkinter.END)
        self.msg_text.insert(0.0, encrypted)

    def decrypt(self):
        message = self.msg.get(0.0, tkinter.END)
        decrypted = e.decrypt_message(message)

        self.msg_text.delete(0.0, tkinter.END)
        self.msg_text.insert(0.0, decrypted)


root = tkinter.Tk()
root.title("Encrypt/Decrypt Tool")
root.geometry("450x250")

app = Application(root)

root.mainloop()