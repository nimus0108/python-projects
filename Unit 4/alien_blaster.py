# Lets go blast some aliens
# hellyeaaa
# Suspacemin Kim

# the player
class Player(object):
    def blast(self, enemy):
        print("The player blasts an enemy.\n")
        enemy.die()

# the alien
class Alien(object):
    def die(self):
        print("The alien gasps and says 'Oh, this is it. This is the big one. \n"
              "Yes, it's getting dark now. Tell my 1.5 million larvae that I loved them...\n" "Good-bye, cruel universe.'")

#main
print("\t\tDeath of an Alien\n")

hero = Player()
invader = Alien()
hero.blast(invader)

input("\n\nPress the enter key to exit")

