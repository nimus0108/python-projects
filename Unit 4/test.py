class Character (object):
    '''
    The maximum dexterity of any character is 100.  This value is used in attack()
    to determine the likelihood of the Character hitting the enemy.
    '''
    MAX_DEXTERITY = 100

    def __init__ (self, name, hit_points, strength, dexterity):
        '''
        Set the instance variables of name, hit_points, strength, and dexerity
        baesd upon the passed parameters.
        '''
        self.name = name
        self.hit_points = int(hit_points)
        self.strength = int(strength)
        self.dexerity = int(dexterity)


file_name = open("battle_characters.txt", "r")
llist = []
for line in file_name:
    line = line.strip()
    linelist = line.split(',')
    llist.append(Character(linelist[0], linelist[1], linelist[2], linelist[3]))
    print(linelist[0],linelist[1], linelist[2], linelist[3])
