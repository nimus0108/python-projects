# Su Min Kim
# Distint Numbers
# November 3

# getting input...
nums = input("")
list1 = nums.split()
ans = ""

# for loop to go through each number
for number in list1:
    # add number to ans with a space if not already there
    if number not in ans:
        ans += (number + " ")

#print final answer
print(ans)
