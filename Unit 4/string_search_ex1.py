
#
# Exercise 1; 
#    - Extract the number between 2nd 'cd' and the 1st 'ef' from the string.
#
str1 ="99578cd6784cd6658ef4875ef55521  "

print (str1)

pos = str1.find("cd")
print(pos)

str1 = str1[pos+2:]
print(str1)

pos = str1.find("cd")
str1 = str1[pos+2:]
print(str1)

pos = str1.find("ef")
str1 = str1[:pos]
print(str1)