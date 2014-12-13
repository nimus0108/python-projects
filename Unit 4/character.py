import random

class Character (object):
    '''
    The maximum dexterity of any character is 100.  This value is used in attack()
    to determine the likelihood of the Character hitting the enemy.
    '''
    MAX_DEXTERITY = 100

    def __init__ (self, name, hit_points, strength, dexerity, shield):
        '''
        Set the instance variables of name, hit_points, strength, and dexerity
        baesd upon the passed parameters.
        '''
        self.name = name
        self.hit_points = int(hit_points)
        self.strength = int(strength)
        self.dexerity = int(dexerity)
        self.shield = int(shield)

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
        selfenemy_total = self.dexerity + enemy.dexerity
        ranint = random.randint(0, selfenemy_total)
        if ranint < self.dexerity:
            drandom = random.randint(0, self.strength)
            if enemy.shield > 0:
                enemy.shield-=1
                print(self.name + " hits " + enemy.name + " causing " + "0" + " damage.")
                print(enemy.name + " used a shield! " + str(enemy.shield) + " shield(s) remaining for " + enemy.name + ".")
            else:
                print(self.name + " hits " + enemy.name + " causing " + str(drandom) + " damage.")
                enemy.hit_points -= drandom
        else:
            print("Close, but that was a miss!")


    def die(self):
        print(self.name + ": Im going to die now")


    def __str__ (self):
        ''' Prints the name, hit points, strength, and dexterity of the object. '''

        print(self.name + ": " + str(self.hit_points) + " " + str(self.strength) + " " + str(self.dexerity) + " " + str(self.shield))

class CharacterList (object):
    def __init__ (self, file_name):
        '''
        This method initializes a new CharacterList object by loading
        a list of Characters from file_name.  The list is stored as an
        instance variable of this CharacterList object.

        The file is in comma, separated format.  The fields of the file include:
            <Name>,<Hit Points>,<Strength>,<Dexterity>
        '''
        file_name = open(file_name, "r")
        llist = []
        for line in file_name:
            line = line.strip()
            linelist = line.split(',')
            llist.append(Character(linelist[0], linelist[1], linelist[2], linelist[3], linelist[4]))
        self.llist = llist
    def print_list (self):
        '''
        Prints the list of characters, using the __str__ function of Character object.
        '''
        index = 1
        for i in self.llist:
            print(str(index) + ":")
            i.__str__()
            index += 1

    def get_and_remove_character (self, i):
        '''
        Gets and returns the "ith" Character from the list, then removes the
        character from the list.  (Doing so prevents the user and computer from
        using the same character.
        '''
        tempi = self.llist[(i-1)]
        self.llist.remove(self.llist[(i-1)])
        return tempi

    def get_random_character (self):
        ''' Gets and returns a random character from the list (for the computer). '''
        return random.choice(self.llist)

    def get_number_of_characters (self):
        ''' Returns the number of characters in the list. '''
        return len(self.llist)