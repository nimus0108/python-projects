import tkinter

class Screen_character_selector (tkinter.Frame):
    def __init__ (self, master, char_list, call_on_selected):
        super(Screen_character_selector, self).__init__(master)
        
        # Save the list of characters 
        self.char_list = char_list
        
        # Save the method reference to which we return control after the player hits "Next"
        self.call_on_selected = call_on_selected
        
        self.grid()
        self.create_widgets()
        
    def create_widgets (self):
        '''
        This method creates all of the widgets character selector page.
        
        The radio buttons on this page must use the variable "self.character".  
        The values of the radio buttons must be a number equally the position of the character in the list. 
        For example, if the characters listed are Troll, Elf, Human, and Dwarf.  self.character would equal 0 
        for the Troll, 1 for the Elf, and so forth.  
        
        The variable self.character has been instantiated for your convenience below.
        
        Here is sample code for including an image on a page:   (char is a Character object)
            imageSmall = tkinter.PhotoImage(file="images/" + char.small_image);
            w= tkinter.Label (self,
                        image = imageSmall,

            w.grid (ADD PARAMETERS HERE)
        '''
        self.character = tkinter.StringVar()
        self.character.set(None)

        tkinter.Label(self, text = "Hit Points").grid(row = 0, column = 2)
        tkinter.Label(self, text = "Dexterity").grid(row = 0, column = 3)
        tkinter.Label(self, text = "Strength").grid(row = 0, column = 4)


        r = 1
        v=0
        for character in self.char_list.character_list:

            tkinter.Radiobutton(self, text = character.name, variable = self.character, value = v).grid(row = r, column = 0, sticky=tkinter.W)
            tkinter.Label(self, text = character.hit_points).grid(row = r, column = 2)
            tkinter.Label(self, text = character.dexterity).grid(row = r, column = 3)
            tkinter.Label(self, text = character.strength).grid(row = r, column = 4)

            imageSmall = tkinter.PhotoImage(file="images/" + character.small_image)
            w= tkinter.Label (self, image = imageSmall)
            w.photo = imageSmall
            w.grid (row = r, column=1)
            w.photo = imageSmall

            r += 1
            v += 1

        tkinter.Button(self, text="Continue to Battle!", command=self.continue_clicked).grid(row=r, column=4)


        #
        # TO DO
        #
       
 
    def continue_clicked(self):
        ''' This method is called when the Next button is clicked. 
            Notice that it passes self.character back to the callback method. '''         
        self.call_on_selected(self.character.get())