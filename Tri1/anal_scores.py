# Su Min Kim
# Analysis Scores

num = input("")
num_list = num.split()
greater = 0
less = 0

def get_mean (num_list):
    m = 0
    i = 0
    x = len(num_list)
    for i in range (0, x):
        number = int(num_list[i])
        m += number

    mean = m/x
    return mean

for num in num_list:
    number = int(num)
    mean = get_mean(num_list)
    
    if number >= mean:
        greater += 1
    else:
        less += 1

print("# of values equal to or greater than the mean: ", greater)
print("# of values less than the mean: ", less)
