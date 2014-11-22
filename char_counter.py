def read_file(file_name):
    text_file = open(file_name, "r")

    my_dict = {}
    for line in text_file:
        for c in line:
            c = c.lower()
            if (c.isalpha()):
                current = my_dict.get(c,0)
                current += 1
                my_dict[c] = current
    return(my_dict)

def main():
    my_dict = read_file("story.txt")
    char_list = list(my_dict.keys())
    char_list.sort()
    for c in char_list:
        print("%s: %d times" % (c, my_dict[c]))

main()
