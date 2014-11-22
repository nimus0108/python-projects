def read_file(file_name):
    text_file = open(file_name, "r")
    my_dict = {}
    
    for c in text_file:
        c = int(c)
        current = my_dict.get(c, 0)
        current += 1
        my_dict[c] = current
    return (my_dict)

def main():
    my_dict = read_file("num_dist_1.txt")
    read_file("num_dist_1.txt")
    char_list = list(my_dict.keys())
    for c in char_list:
        if my_dict[c] > 1:
            print("%s: %d times" % (c, my_dict[c]))
        else:
            print("%s: %d time" % (c, my_dict[c]))
main()
