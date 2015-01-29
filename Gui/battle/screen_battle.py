import tkinter

class Screen_Battle (tkinter.Frame):
    def __init__ (self, master, player1, player2, call_on_next):
        super(Screen_Battle, self).__init__(master)

        # Save references to the two player objects
        self.player1 = player1
        self.player2 = player2

        # Store the maximum number of hit points which are needed on the screen display.
        self.player1_max_hp = player1.hit_points
        self.player2_max_hp = player2.hit_points

        # Save the method reference to which we return control after this page Exits.
        self.call_on_selected = call_on_next

        self.create_widgets()
        self.grid()
        
    def create_widgets (self):
        tkinter.Label(self, text="You").grid(row=0, column=0)
        tkinter.Label(self, text="Computer").grid(row=0, column=1)


        imageLarge = tkinter.PhotoImage(file="images/" + self.player1.large_image)
        w = tkinter.Label (self, image=imageLarge)
        w.photo = imageLarge
        w.grid (row = 4, column=0)

        imageLarge = tkinter.PhotoImage(file="images/" + self.player2.large_image)
        w = tkinter.Label (self, image=imageLarge)
        w.photo = imageLarge
        w.grid (row = 4, column=1)

        self.attack_button = tkinter.Button(self, text="Attack", command=self.attack_clicked)
        self.attack_button.grid(row=1, column=0)

        self.label1 = tkinter.Label(self, text="")
        self.label1.grid(row=1, column=1)
        self.label2 = tkinter.Label(self, text="")
        self.label2.grid(row=2, column=1)

        tkinter.Label(self, text=str(self.player1.hit_points) + "/" + str(self.player1_max_hp) + " HP").grid(row=5, column=0)
        tkinter.Label(self, text=str(self.player2.hit_points) + "/" + str(self.player2_max_hp) + " HP").grid(row=5, column=1)


        
    def attack_clicked(self):
        ''' This method is called when the use following:
            1) Calls the character.attack method for both the player and the computer.
            2) Updates the labels on the top right with the result of the attacks.
            3) Determines if there is a victor.
            4) If there is a victor, removes that Attack button and replaces it with an Exit button.     
        '''

        result = self.player1.attack(self.player2)
        self.label1["text"] = result
        result = self.player2.attack(self.player1)
        self.label2["text"] = result

        if (self.player1.hit_points<0 and self.player2.hit_points<0):
            tkinter.Label(self, text="It is a tie!").grid(row=3, column=1)
            self.attack_button.destroy()
            tkinter.Button(self,text="Exit", command=self.exit_clicked).grid(row=6, column=1, sticky = tkinter.E)
        elif(self.player1.hit_points < 0):
            tkinter.Label(self, text = self.player2.name + " is victorious!").grid(row=3, column=1)
            self.attack_button.destroy()
            tkinter.Button(self,text="Exit", command=self.exit_clicked).grid(row=6, column=1, sticky = tkinter.E)
        elif(self.player2.hit_points < 0):
            tkinter.Label(self, text = self.player1.name + " is victorious!").grid(row=3, column=1)
            tkinter.Button(self,text="Exit", command=self.exit_clicked).grid(row=6, column=1, sticky = tkinter.E)
            self.attack_button.destroy()


        tkinter.Label(self, text=str(self.player1.hit_points) + "/" + str(self.player1_max_hp) + " HP").grid(row=5, column=0)
        tkinter.Label(self, text=str(self.player2.hit_points) + "/" + str(self.player2_max_hp) + " HP").grid(row=5, column=1)
    def exit_clicked(self):
        ''' This method is called when the Exit button is clicked. 
            It passes control back to the callback method. '''        
        self.call_on_selected()