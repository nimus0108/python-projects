# Su Min Kim
# 10-28
# Exercise: Counting Vowels and Consonants

#defining consonants and vowels
consonants = "bcdfghjklmnpqrstvwxyz"
vowels = "aeiou"

#Counting consonants
def count_consonants (my_str):
    cc = 0
    my_str = Imy_str.lower()
    #for loop for each index number
    for i in range (0, len(my_str)):
        if my_str[i] in consonants:
            cc += 1
    #returns the number of consonants
    return cc

#Counting vowels
def count_vowels (my_str):
    vc = 0
    my_str = my_str.lower()
    #for loop for each index number
    for i in range (0, len(my_str)):
        if my_str[i] in vowels:
            vc += 1
    #Return vowelIm  count
    return vc

def main ():
    x = input("Input: ")
    print("consonants:", count_consonants(x),"\nvowels:",
          count_vowels(x))


main()
