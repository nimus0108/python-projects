import tkinter

class Screen_prepare_to_battle (tkinter.Frame):
    def __init__ (self, master, player1, player2, call_on_next):
        super(Screen_prepare_to_battle, self).__init__(master)

        # Save player character object references
        self.player1 = player1
        self.player2 = player2
        
        # Save the method reference to which we return control after the player hits "Next"
        self.call_on_selected = call_on_next
        
        self.create_widgets()
        self.grid()
        
    
    def create_widgets (self):
        '''
        This method creates all of the widgets the prepare to battle page.
        '''
        tkinter.Label(self, text="You").grid(row=0, column=0)
        tkinter.Label(self, text="Computer").grid(row=0, column=1)


        imageLarge = tkinter.PhotoImage(file="images/" + self.player1.large_image)
        w = tkinter.Label (self, image=imageLarge)
        w.photo = imageLarge
        w.grid (row = 1, column=0)

        imageLarge = tkinter.PhotoImage(file="images/" + self.player2.large_image)
        w = tkinter.Label (self, image=imageLarge)
        w.photo = imageLarge
        w.grid (row = 1, column=1)

        tkinter.Label(self, text = str(self.player1.hit_points) + " HP").grid(row = 2, column = 0)
        tkinter.Label(self, text = str(self.player1.dexterity) + " Dexterity").grid(row = 3, column = 0)
        tkinter.Label(self, text = str(self.player1.strength) + " Strength").grid(row = 4, column = 0)

        tkinter.Label(self, text = str(self.player2.hit_points) + " HP").grid(row = 2, column = 1)
        tkinter.Label(self, text = str(self.player2.dexterity) + " Dexterity").grid(row = 3, column = 1)
        tkinter.Label(self, text = str(self.player2.strength) + " Strength").grid(row = 4, column = 1)

        tkinter.Button(self, text = "Let's Battle", command=self.continue_clicked).grid(row=5, column=1, sticky=tkinter.E)

 
    def continue_clicked(self):
        ''' This method is called when the Battle button is clicked. 
            It passes control back to the callback method. '''         
        self.call_on_selected()
