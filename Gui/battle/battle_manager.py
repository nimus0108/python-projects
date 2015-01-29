import tkinter

#
# No changes are required in this file.
#

from Gui.battle.screen_battle import Screen_Battle
from Gui.battle.screen_prepare_to_battle import Screen_prepare_to_battle
from Gui.battle.screen_pick_character import Screen_character_selector
from Gui.battle.characters import CharacterList

class Battle_Manager (object):
    
    def __init__ (self):
        '''
        Initializes a new battle manager by loading the list of characters from the file and
        by initializing tkinter.
        '''
        self.character_choices = CharacterList ("battle_characters.txt")
        self.root = tkinter.Tk()
    
    def setup_character_selector (self):
        ''' This method is called to create the CharacterSelector screen. '''        
        self.root.title ("Select your character!")    
        self.char_sel = Screen_character_selector(self.root, self.character_choices, self.onclose_character_selector)    
               
    def onclose_character_selector (self, selected_char):
        ''' This method is called when the Screen_character_selector closes. 
            selected_char should contain the index in the list of the character selected by the user. 
            The method manages the assignment of the player and computer objects and then starts the 
            Prepare for Battle page.
            '''        
        selected_char = int(selected_char)
        
        # Saves players character choice
        self.player = self.character_choices.get_and_remove_character(selected_char)
        
        # Gets a player for the computer.
        self.computer = self.character_choices.get_random_character()
        
        # Destroys the "Character Selection" frame`
        self.char_sel.destroy()

        # Retitle the main frame.
        self.root.title ("The Combatants!")
        
        # Creates the "Prepare to Battle" frame
        self.prepare = Screen_prepare_to_battle(self.root, self.player, self.computer, self.onclose_prepare_to_battle)
    
    def onclose_prepare_to_battle (self):
        ''' 
        This method is called when the user presses button on the Prepare to Battle screen.
        The method closes the current window and creates the battle window.
        '''
        # Destroy the "Prepare to Battle" frame.
        self.prepare.destroy()

        # Retitle the main frame.
        self.root.title ("Battle!")
    
        # Create the Battle frame
        self.battle_screen = Screen_Battle(self.root, self.player, self.computer, self.onclose_battle)

    def onclose_battle (self):
        ''' This method is called after the battle is over.  This method causes the program to exit. '''
        self.root.destroy()
        
def main():
    battle = Battle_Manager()
    battle.setup_character_selector()
    battle.root.mainloop()
 
main()