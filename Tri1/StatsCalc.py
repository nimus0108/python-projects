# Su Min Kim
# Stats Calc

import math

def read_numbers_from_file(file_name):
    text_file = open(file_name, "r")

    num_nmbrs = int(text_file.readline())
    num_list = []

    for i in range (0, num_nmbrs):
        next_num = int(text_file.readline())
        num_list.append(next_num)

    num_list.sort()
    return num_list

def read_numbers ():
    num_list=[]
    x = int(input("How many numbers will you put in?"))
    print("input:")
    for x in range (0, x):
        num = int(input(""))
        num_list.append(num)
    return num_list

def get_mean (num_list):
    m = 0
    i = 0
    x = len(num_list)
    for i in range (0, x):
        m += num_list[i]

    mean = m/x
    return mean

def get_range (num_list):
    maxn = max(num_list)
    minn = min(num_list)
    return(maxn - minn)

def get_median(num_list):
    x = len(num_list)
    num_list.sort()
    if (x%2) != 0:
        idx = int(x/2)
        return num_list[idx]
    
    elif (x%2)==0:
        i1 = int((x/2)-1)
        i2 = int(x/2)
        median = (num_list[i1] + num_list[i2])/2
        return median

def get_std_dev (num_list):
    mean = get_mean(num_list)
    diss = 0
    for num in num_list:
        if num > mean:
            diss += (num - mean) ** 2
        else:
            diss += (mean - num) ** 2
    std_dev_avg = diss/(len(num_list))
    std_dev_ans = math.sqrt(std_dev_avg)
    return std_dev_ans

def get_min (num_list):
    return min(num_list)

def get_max (num_list):
    return max(num_list)

def main():
    my_list = read_numbers_from_file("test_num_1.txt")
    print ("Mean: ", get_mean(my_list))
    print ("Std Dev: ", get_std_dev(my_list))
    print ("Median: ", get_median(my_list))
    print ("Min: ", get_min(my_list))
    print ("Max: ", get_max(my_list))
    print ("Range: ", get_range(my_list))
    
main()
