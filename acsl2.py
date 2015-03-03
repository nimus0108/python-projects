import re
inputlist = []
outputlist = []
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []

#input into inputlist
for i in range (1,6):
    tempInput = input(str(i) + ". ")
    tempInput = tempInput.replace("'", "")
    tempInput = tempInput.replace("(", "", 1)
    tempInput = tempInput[:-1]
    inputlist.append(tempInput)

#input into specific list
#temp input list item
tili= inputlist[0]
i = 0
#list 1
while i<len(tili):
    if tili[i] == "(":
        i += 1
        addthis = "("
        while tili[i] != ")":
            current = tili[i]
            addthis += current
            i+=1
        list1.append(addthis+")")
        i+=1
    elif tili[i] == " ":
        i+=1
    else:
        list1.append(tili[i])
        i+=1
#list 2
i=0
tili= inputlist[1]
while i<len(tili):
    if tili[i] == "(":
        i += 1
        addthis = "("
        while tili[i] != ")":
            current = tili[i]
            addthis += current
            i+=1
        list2.append(addthis+")")
        i+=1
    elif tili[i] == " ":
        i+=1
    else:
        list2.append(tili[i])
        i+=1
#list 3
i=0
tili= inputlist[2]
while i<len(tili):
    if tili[i] == "(":
        i += 1
        addthis = "("
        while tili[i] != ")":
            current = tili[i]
            addthis += current
            i+=1
        list3.append(addthis + ")")
        i+=1
    elif tili[i] == " ":
        i+=1
    else:
        list3.append(tili[i])
        i+=1
#list 4
i=0
tili= inputlist[3]
while i<len(tili):
    if tili[i] == "(":
        i += 1
        addthis = "("
        while tili[i] != ")":
            current = tili[i]
            addthis += current
            i+=1
        list4.append(addthis + ")")
        i+=1
    elif tili[i] == " ":
        i+=1
    else:
        list4.append(tili[i])
        i+=1
#list 5
i=0
tili= inputlist[4]
while i<len(tili):
    if tili[i] == "(":
        i += 1
        addthis = "("
        while tili[i] != ")":
            current = tili[i]
            addthis += current
            i+=1
        list5.append(addthis +")")
        i+=1
    elif tili[i] == " ":
        i+=1
    else:
        list5.append(tili[i])
        i+=1


answer1 = "'("
for i in range(0, len(list1)):
    index = len(list1) - i - 1
    answer1 += list1[index] + " "
answer1 += ")"
print("1. " +answer1)


answer2 = "'("
i=0
breaked = False
while i < len(list2):
    tatom = list2[i]
    tatom2 = list2[i+1]
    if tatom == tatom2:
        counter = 1
        while(tatom==tatom2):
            counter += 1
            i += 1
            if (i+1) > (len(list2)-1):
                breaked = True
                break
            tatom = list2[i]
            tatom2 = list2[i+1]
        answer2 += "(" + str(counter) + " " + tatom+ ")"
        i+=1
    elif tatom == " ":
        i+=1
        pass
    else:
        answer2 += "(1 "+tatom+")"
        i+=1

    if ((i+1) > (len(list2)-1)) and (breaked==False):
        answer2 += "(1 " + str(list2[i] + ")")
        break

answer2 += ")"
print("2. " + answer2)

answer3 = "'("
breaked=False
i=0
while i < len(list3):
    tatom = list3[i]
    tatom2 = list3[i+1]
    if tatom == tatom2:
        counter = 1
        while(tatom==tatom2):
            counter += 1
            i += 1
            if (i+1) > (len(list3)-1):
                breaked = True
                break
            tatom = list3[i]
            tatom2 = list3[i+1]
        answer3 += "(" + str(counter) + " " + tatom+ ")"
        i+=1
    elif tatom == " ":
        i+=1
        pass
    else:
        answer3 += " "+tatom+" "
        i+=1

    if ((i+1) > (len(list2)-1)) and (breaked==False):
        answer3 += "(1 " + str(list2[i] + ")")
        break

answer3 += ")"
print("3. " +answer3)
answer4 = "'("
i = 1
se = list4[-1] #special element
while i < len(list4)+1:
    if (i%int(se) == 0):
        pass
    else:
        answer4 += list4[i-1]
    i += 1
answer4 += ")"
print("4. " + answer4)

answer5 = ""
num = int(list5[-1])
i=0
while(i < len(list5)-1):
    answer5 += "'("
    for index in range (i, i+num):
        answer5 += list5[index]
    i+=num
    answer5+=") "

answer5 = answer5[:-2]
answer5 += list5[-1]
answer5 += ")"

print("5. " + answer5)
