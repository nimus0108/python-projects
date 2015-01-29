import tkinter
from Gui.Encryptor import Encryptor

e = Encryptor("cipher1.txt")

print("E - Encrypt a message")
print("D - Decrypt a message")
print("Q - Quit")

choice = input("")

while(choice!="Q"):

    if choice == "E":
        msg = input("Enter your message to encrypt.\n")
        print(e.encrypt_message(msg))
    elif choice == "D":
        msg = input("Enter the secret message.\n")
        print(e.decrypt_message(msg))
    else:
        print("Invalid option\n")

    print("\nE - Encrypt a message")
    print("D - Decrypt a message")
    print("Q - Quit")

    choice = input("")