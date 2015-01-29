class Encryptor (object):
    
    def __init__ (self, file_name):   
        ''' 
        Initializes a new encryption object, using the cypher from the specified file
        '''    
        text_file = open(file_name,"r")
        self.e_dict = {}
        self.d_dict = {}
        
        for line in text_file:
            encrypted = line.split()
            self.e_dict[encrypted[0]] = encrypted[1]
            self.d_dict[encrypted[1]] = encrypted[0]
        
        text_file.close()
    
    def encrypt_message (self, msg):
        ''' Returns an encrypted message. '''
        msg = msg.upper()
        #self.encryption.insert(0.0, self.msg)
        return self.__write_message (msg, self.d_dict)
    
    def decrypt_message (self, msg):
        ''' Returns a decrypted message. '''
        msg = msg.upper()
        return self.__write_message (msg, self.e_dict)
    
    def __write_message (self, msg, my_dict):    
        out_msg = ""
        for c in msg:
            out_msg += my_dict.get(c,c)

        return out_msg
        
