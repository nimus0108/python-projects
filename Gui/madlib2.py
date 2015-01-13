import tkinter

class Application(tkinter.Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        tkinter.Label(self, text="MADLIB").grid(row=0, column=0, columnspan=3, sticky=tkinter.W)

        # Name
        tkinter.Label(self,text = "Player 1: ").grid(row = 1, column = 0, sticky = tkinter.W)
        self.player1_ent = tkinter.Entry(self)
        self.player1_ent.grid(row = 1, column = 1, sticky = tkinter.W)

        # Second name
        tkinter.Label(self,
              text = "Player 2: ").grid(row = 2, column = 0, sticky = tkinter.W)
        self.player2_ent = tkinter.Entry(self)
        self.player2_ent.grid(row = 2, column = 1, sticky = tkinter.W)

        # Year
        tkinter.Label(self,
              text = "Year: ").grid(row = 3, column = 0, sticky = tkinter.W)
        self.year_ent = tkinter.Entry(self)
        self.year_ent.grid(row = 3, column = 1, sticky = tkinter.W)

        # Integer
        tkinter.Label(self, text="Integer:").grid(row=4, column=0, sticky=tkinter.W)
        self.integer_ent = tkinter.Entry(self)
        self.integer_ent.grid(row=4, column=1, sticky = tkinter.W)

        # Average
        tkinter.Label(self,
              text = "Number:"
              ).grid(row = 5, column = 0, sticky = tkinter.W)

        self.average = tkinter.StringVar()
        self.average.set(None)

        averages = ["0.124", "0.315", "0.762"]
        column = 1
        for average in averages:
            tkinter.Radiobutton(self,
                        text = average,
                        variable = self.average,
                        value = average).grid(row = 5, column = column, sticky = tkinter.W)
            column += 1

        # Adjectives
        tkinter.Label(self, text="Player 2 was: ")
        self.handsome = tkinter.BooleanVar()
        tkinter.Checkbutton(self,
                    text = "Handsome",
                    variable = self.handsome
                    ).grid(row = 6, column = 1, sticky = tkinter.W)

        self.crazy = tkinter.BooleanVar()
        tkinter.Checkbutton(self,
                    text = "Crazy",
                    variable = self.crazy
                    ).grid(row = 6, column = 2, sticky = tkinter.W)

        self.weird = tkinter.BooleanVar()
        tkinter.Checkbutton(self,
                    text = "Weird",
                    variable = self.weird
                    ).grid(row = 6, column = 3, sticky = tkinter.W)


        # Tell Story
        tkinter.Button(self,
               text = "Click for story",
               command = self.tell_story
               ).grid(row = 7, column = 0, sticky = tkinter.W)

        self.story_txt = tkinter.Text(self, width = 75, height = 10, wrap = tkinter.WORD)
        self.story_txt.grid(row = 8, column = 0, columnspan = 4)

    def tell_story(self):
        year = self.year_ent.get()
        player1 = self.player1_ent.get()
        player2 = self.player2_ent.get()
        integer = self.integer_ent.get()
        average = self.average.get()
        p1hr = 36
        p2hr = p1hr + int(integer);

        adj = ""
        if self.handsome.get():
            adj += ", handsome"
        if self.weird.get():
            adj += ", weird"
        if self.crazy.get():
            adj += ", crazy"


        story = "In "
        story += year
        story += ", the most interesting baseball rivalry broke out. It was between the two players "
        story += player1
        story += " and "
        story += player2
        story += ". "
        story += player1 + " was mean" + adj + ", and big. "
        story += player2 + " was nice. "
        story += "However, both players were legendary shortstops. "
        story += player1 + " played for the Yankees and " + player2 + " for the Orioles. "
        story += "That year, " + player1 + " had the higher average with " + average + ". "
        story += "However, "+ player2 + " had " + integer + " more home runs, " + str(p1hr) +", while " + player1 + " had " + str(p2hr) + ". "
        story += "Unfortunetly, the world could not conclude who was the best shortstop, " + player1 + " or " + player2 + ", because of a new, much better shortstop named Derek Jeter."
        story += " #RE2PECT"

        self.story_txt.delete(0.0, tkinter.END)
        self.story_txt.insert(0.0, story)


root = tkinter.Tk()
root.title("Su Min - Mad Lib")
app = Application(root)
root.mainloop()