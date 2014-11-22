

def load_file (file_name):
    text_file = open (file_name, "r")
    my_dict = {}
    for line in text_file:
        acronym = line.split(":")
        the_name = acronym[0]
        the_def = acronym[1].strip()
        my_dict[the_name] = the_def
    return my_dict

def get_user_next_choice(key_list):
    print("Which def would u like?")
    for w in key_list:
        print(w, end = " ")
    return input()

def main():
    my_dict = load_file ("definitions.txt")
    key_list = list(my_dict.keys())
    key_list.sort()

    choice = get_user_next_choice(key_list)
    while (choice != "quit"):
        word_def = my_dict.get(choice, "oiwgwoiegjAGAIN")
        print(word_def + "\n\n")
        choice = get_user_next_choice(key_list)
        
main()
