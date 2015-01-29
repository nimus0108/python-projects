import random

#
# No changes are required in this file.
#
 
class Character (object):
   
    def __init__ (self, name, hit_points, strength, dexterity, small_image, large_image):
        ''' 
        Set the instance variables of name, hit_points, strength, and dexerity
        based upon the passed parameters. 
        '''
        self.name = name
        self.hit_points = hit_points
        self.strength = strength
        self.dexterity = dexterity
        self.small_image = small_image
        self.large_image = large_image
        
    def attack (self, enemy):
        ''' 
        In this method, self attempts to attack the enemy.  First, the method determines if 
        a hit occurs using randomness.  If the opponents had the same dexterity, the probability 
        of a hit would be 50%.  If the dexterity of self is higher than that of enemy, the probability
        of a hit increases.  If the dexterity of self is lower than that of enemy, the probability
        of a hit decreases.  The exact implementation of this probability is up to you, but 
        make it as fair as possible.
        
        If a hit occurs, hit_points damage should be a random number between 0 and the self.strength.
        
        The method should then print the result of the attack to the user.
        '''
        
        total_dex = self.dexterity + enemy.dexterity
        hit_attempt = random.randrange(0,total_dex)        
        if (hit_attempt<=self.dexterity):
            damage = random.randrange (0, self.strength)
            enemy.hit_points -= damage
            result = self.name + " hits " + enemy.name +" causing " + str(damage) + " damage."
        else:
            result = self.name + " misses " + enemy.name + "."
                            
        return result
        
    def die (self):
        ''' Prints a death message. '''
        print (self.name + ": Ahhhhh.. too much damage!  I have died.")
        
    def __str__ (self):
        ''' Prints the name, hit points, strength, and dexterity of the object. '''
        return self.name + "; HP: " + str(self.hit_points) + "; Strength: " + str(self.strength) + "; Dexterity: " + str(self.dexterity)        
        
class CharacterList (object):
    def __init__ (self, file_name):
        ''' 
        This method intializes a new CharacterList object by loading
        a list of Characters from file_name.  
        The file is in comma, separated format.  The fields of the file include:
            <Name>,<Hit Points>,<Strength>,<Dexterity>
        '''
        self.character_list = []
        
        text_file = open(file_name,"r")
        
        for line in text_file:
            line = line.strip()
            my_fields = line.split(",")
            character = Character (my_fields[0], int(my_fields[1]), int(my_fields[2]), int(my_fields[3]), my_fields[4], my_fields[5])
            self.character_list.append(character)
    
    def print_list (self):
        ''' 
        Prints the list of characters_base, using the __str__ function of Character object.
        '''
        for i in range (len(self.character_list)):
            print (str(i) +": " + str(self.character_list[i]))        
    
    def get_and_remove_character (self, i):
        ''' 
        Gets and returns the "ith" Character from the list, then removes the 
        character from the list.  (Doing so prevents the user and computer from 
        using the same character.
        '''
        ch = self.character_list[i]
        self.character_list.remove(self.character_list[i])
        return ch
    
    def get_random_character (self):
        ''' Gets and returns a random character from the list (for the computer). '''
        return random.choice(self.character_list)
    
    def get_number_of_characters (self):
        ''' Returns the number of characters_base in the list. '''
        return len(self.character_list)