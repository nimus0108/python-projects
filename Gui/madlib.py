# Mad Lib
# Create a story based on user input

import tkinter

class Application(tkinter.Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        tkinter.Label(self,
              text = "Enter information for a new story"
              ).grid(row = 0, column = 0, columnspan = 2, sticky = tkinter.W)

        tkinter.Label(self,
              text = "Person: "
              ).grid(row = 1, column = 0, sticky = tkinter.W)
        self.person_ent = tkinter.Entry(self)
        self.person_ent.grid(row = 1, column = 1, sticky = tkinter.W)

        tkinter.Label(self,
              text = "Plural Noun:"
              ).grid(row = 2, column = 0, sticky = tkinter.W)
        self.noun_ent = tkinter.Entry(self)
        self.noun_ent.grid(row = 2, column = 1, sticky = tkinter.W)

        tkinter.Label(self,
              text = "Verb:"
              ).grid(row = 3, column = 0, sticky = tkinter.W)
        self.verb_ent = tkinter.Entry(self)
        self.verb_ent.grid(row = 3, column = 1, sticky = tkinter.W)

        tkinter.Label(self,
              text = "Adjective(s):"
              ).grid(row = 4, column = 0, sticky = tkinter.W)

        self.is_itchy = tkinter.BooleanVar()
        tkinter.Checkbutton(self,
                    text = "itchy",
                    variable = self.is_itchy
                    ).grid(row = 4, column = 1, sticky = tkinter.W)

        self.is_joyous = tkinter.BooleanVar()
        tkinter.Checkbutton(self,
                    text = "joyous",
                    variable = self.is_joyous
                    ).grid(row = 4, column = 2, sticky = tkinter.W)

        self.is_electric = tkinter.BooleanVar()
        tkinter.Checkbutton(self,
                    text = "electric",
                    variable = self.is_electric
                    ).grid(row = 4, column = 3, sticky = tkinter.W)

        tkinter.Label(self,
              text = "Body Part:"
              ).grid(row = 5, column = 0, sticky = tkinter.W)

        self.body_part = tkinter.StringVar()
        self.body_part.set(None)

        body_parts = ["bellybutton", "big toe", "medulla oblongata"]
        column = 1
        for part in body_parts:
            tkinter.Radiobutton(self,
                        text = part,
                        variable = self.body_part,
                        value = part
                        ).grid(row = 5, column = column, sticky = tkinter.W)
            column += 1

        tkinter.Button(self,
               text = "Click for story",
               command = self.tell_story
               ).grid(row = 6, column = 0, sticky = tkinter.W)

        self.story_txt = tkinter.Text(self, width = 75, height = 10, wrap = tkinter.WORD)
        self.story_txt.grid(row = 7, column = 0, columnspan = 4)

    def tell_story(self):
        person = self.person_ent.get()
        noun = self.noun_ent.get()
        verb = self.verb_ent.get()
        adjectives = ""
        if self.is_itchy.get():
            adjectives += "itchy, "
        if self.is_joyous.get():
            adjectives += "joyous, "
        if self.is_electric.get():
            adjectives += "electric, "
        body_part = self.body_part.get()

        story = "The famous explorer "
        story += person
        story += " had nearly given up a life-long quest to find The Lost City of "
        story += noun.title()
        story += " when one day, the "
        story += noun
        story += " found "
        story += person + ". "
        story += "A strong, "
        story += adjectives
        story += "peculiar feeling overwhelmed the explorer. "
        story += "After all this time, the quest was finally over. A tear came to "
        story += person + "'s "
        story += body_part + ". "
        story += "And then, the "
        story += noun
        story += " promptly devoured "
        story += person + ". "
        story += "The moral of the story? Be careful what you "
        story += verb
        story += " for."

        self.story_txt.delete(0.0, tkinter.END)
        self.story_txt.insert(0.0, story)

root = tkinter.Tk()
root.title("Mad Lib")
app = Application(root)
root.mainloop()