text_file = open("words.txt", "r")

my_list = []

for line in text_file:
    words = line.split()
    my_list += words

my_list.sort()

print(my_list)
