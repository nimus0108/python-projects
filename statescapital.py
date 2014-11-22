
import random

# Dictionary of the valid quizzes available to the user.
# The key is the label and the value is the data file name.
data_files = {"East": "states_east.txt",
              "West": "states_west.txt",
              "South": "states_south.txt",
              "Central": "states_central.txt",
              "All": "states_all.txt"
              }    

def read_states_into_dict (file_name):
    text_file = open(file_name, "r")
    dict = {}
    for i in text_file:
        i = i.strip()
        list1 = i.split("\t")
        dict[list1[0]] = list1[1]
    return dict            

    """
    Loads the specified text file.  
    There is one State / Capital combination per line.
    The state and capital are separated by a tab character.
    Hint: It is advisable to call strip() on the capital string prior to adding 
    it to the dictionary to remove the new line character.
    """

def quiz (my_dict):
    answer = ""
    counter = 0
    cc = 0
    while (len(my_dict)!=0) and (answer != "quit"):
        state = random.choice(list(my_dict.keys()))
        answer = input("What is the capital of " + state + "?\n")
        if answer == my_dict.get(state, 0):
            print("Correct!")
            del(my_dict[state])
            cc += 1
            counter += 1
        elif answer == "quit":
            my_dict = {}
        elif answer != state:
            print("Incorrect! The capital is", my_dict.get(state,0))
            counter += 1

    print ("Wow! You got",cc,"correct in",counter,"guesses")
    
    """ 
    This method implements a loop that will continue to quiz the user until the user types
    "quit" or correctly identifies all of the capitals in the list.

    Each time the user identifies a capital, it is removed from the list.

    At the end, the function will report how many guesses were required by the user.
    """
    
    
def get_datafile_choice():
    region = input("Which data file would you like to load?\nSouth All West Central East\n")
    if region == "East":
        region = "states_east.txt"
    elif region == "West":
        region = "states_west.txt"
    elif region == "South":
        region = "states_south.txt"
    elif region == "Central":
        region = "states_central.txt"
    elif region == "All":
        region = "states_all.txt"
    else:
        while region != "East" or region != "North" or region != "South" or region != "Central" or region != "All":
            region = input("Invalid submission, resubmit:\nSouth All West Central East\n")
    return region
    
    """ 
    Asks the user to select a data file to use for the quiz.  The function makes sure the 
    user makes a valid selection.  
    The function returns the filename selected by the user.
    """

def main ():
    file_name = get_datafile_choice()
    my_dict = read_states_into_dict (file_name)
    quiz(my_dict)

main()
