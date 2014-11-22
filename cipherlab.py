import random

e_dict = {}  # Global Variable; Encryption dictionary
d_dict = {}  # Global Variable; Decryption dictionary

def create_key ():
    """ 
    OPTIONAL function -- only create this one once you have completed everything else!

    Creates a new random cipher key and prints the key to the console.  
    The user needs to copy this key into a file if desired.    
    """ 

def load_cipher_file (file_name):
    text_file = open(file_name, "r")
    return text_file
    
    for i in text_file:
        list1 = i.split("\t")
        e_dict[list1[0]] = list1[1]
    print(e_dict)

    """ 
    Loads a cipher from the specified file.
    This function sets e_dict to encrypt messages and d_dict to decrypt messages.
    """ 


def encrypt_message ():
    text_file = load_cipher_file (file_name)
    em = ""

    """ 
    This function asks the user for a message to encrypt.
    It then prints an encrypted version of the message.    

    It is ok if the user enters characters that are not ciphered.  In this case, the 
    character entered by the user will pass directly into the output ciphered message
    without being altered.
    """     

def decrypt_message ():
    """ 
    This function asks the user for a message to decrypt.
    It then prints the decrypted message.    

    If a character in the message is not in the cipher dictionary, print the character
    directly to the output without altering it.
    """ 


def main():
    fname = input("Enter the filename of the cipher to use.\n")
    file = load_cipher_file(fname)
    action = " "
    action = input("C - Create a new cypher key\nE - Encrypt a message\nD - Decrypt a message\nQ - Quit")
    while action!= "Q":
        if action == "E":
            print(encrypt_message())
        elif action == "D":
            print(decrypt_message())
        elif action == "C":
            print()
    
    """
    Asks the user which cipher file to load.
    Calls load_cipher_file to load the dictionaries.
    Prints the menu.
    Loops until the user decides to quit.
    Calls encrypt_message and decrypt_message as requested by the user.
    """

main()
