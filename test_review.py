#PROBLEM 1

for i in range (4,17,2):
    print(i)

#PROBLEM 2

print("%6s%15s" % ("Inches", "Centimeters"))
for i in range (5, 96, 9):
    c = i*2.54
    print("%6s%15s" % (i, c))
    
#PROBLEM 3
def largest(a,b,c):
    if a < b:
        ans = b
    else:
        ans = c
    if ans < c:
        ans = c
    return ans

#PROBLEM 4
def mean(my_list):
    add = 0
    for i in my_list:
        add += i
    mean = add/len(my_list)
    return mean

#PROBLEM 5
def position_of_largest(my_list):
    ans = 0
    for i in range (0,len(my_list),1):
        li = my_list[i]
        if li > ans:
            ans = li
            aidx = i
    return aidx

position_of_largest( [25, 4, 5, 25,3])

#PROBLEM 6
ans = 0
list  = input("input list\n")
l1 = list.split()
for i in l1:
    ans += float(i)
print(ans)

#PROBLEM 7
def order_names():
    n = input("how many r u gonna enter huh?")
    i = 0
    list1 = []
    for i in range (0, int(n)):
        item = input("")
        list1.append(item)
    list1.sort()
    for i in list1:
        print(i)
order_names()


#PROBLEM 8
print("%5s%10s%10s%8s" % ("Miles", "KM", "KM", "Miles"))
km2 = 3
for m1 in range (5, 96, 10):
    km1 = m1/0.62
    m2 = km2*0.62
    print("%-5d%10.1f%10d%8.1f" % (m1, km1, km2, m2))
    km2 += 4

#Problem 9
def count_vowels(my_str):
    VOWELS = "AEIOU"
    count = 0
    my_str = my_str.upper()
    for i in my_str:
        if i in VOWELS:
            count += 1
    print(my_str+ ":", count)

count_vowels("sdghj")

#Problem 10
state_birds = {"NJ":"American goldfinch",
 "NY":"Eastern bluebird",
 "CT":"American robin",
 "PA":"Ruffed grouse"}

state = input("Choose a state:\n")
if state in state_birds:
    bird = (state_birds.get(state))
    print("The state bird of", state, "is the", bird+".")
else:
    print("Your choice was not in the list.")

#Problem 11
def get_scores():
    input1 = input("Enter a list of names and scores:\n")
    dict1 = {}
    while (len(input1) > 0):
        x = input1.split(" ")
        dict1[x[0]] = x[1]
        input1 = input("")
    print(dict1)
get_scores()

#PROBLEM 12
i = 28
while (i>7):
    print(i)
    i -= 4
