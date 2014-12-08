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
    
    for line in text_file:
        char = line.split("\t")
        key = char[0]
        v = char[1].strip()
        e_dict[key] = v
        d_dict[v] = key
    """ 
    Loads a cipher from the specified file.
    This function sets e_dict to encrypt messages and d_dict to decrypt messages.
    """ 


def encrypt_message ():
    m = input("input the message\n")
    m = m.upper()

    encrypted = ""

    for i in m:
        encrypted += (d_dict.get(i,i))

    return (encrypted)
        
    """ 
    This function asks the user for a message to encrypt.
    It then prints an encrypted version of the message.    

    It is ok if the user enters characters that are not ciphered.  In this case, the 
    character entered by the user will pass directly into the output ciphered message
    without being altered.
    """     

def decrypt_message ():
    m = input("Enter the message to decrypt\n")
    m = m.upper()

    decrypted = ""

    for i in m:
        decrypted += (e_dict.get(i,i))

    return (decrypted)
        
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
    action = input("\tC - Create a new cypher key\n\tE - Encrypt a message\n\tD - Decrypt a message\n\tQ - Quit\n\n")
    while action!= "Q":
        if action == "E":
            print(encrypt_message())
        elif action == "D":
            print(decrypt_message())
        elif action == "C":
            print()
        action = input("\n\tC - Create a new cypher key\n\tE - Encrypt a message\n\tD - Decrypt a message\n\tQ - Quit\n\n")

    
    """
    Asks the user which cipher file to load.
    Calls load_cipher_file to load the dictionaries.
    Prints the menu.
    Loops until the user decides to quit.
    Calls encrypt_message and decrypt_message as requested by the user.
    """

main()
