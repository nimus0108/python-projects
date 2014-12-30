bdist = {"A": 450, "B": 140, "C": 120, "D": 320, "E": 250, "F": 80}
letters = {"A": 0, "B": 1, "C": 2, "D":3, "E": 4, "F": 5, "G": 6}
vehicle = {'C': 28, 'M': 25, 'F':22, 'V':20}
roads = {'I': 65, 'H':60, 'M':55, 'S':45}
keylist = ["A", "B", "C", "D", "E", "F"]
output1 = []
output2 = []
output3 = []
output4 = []

for i in range(0, 5):
    input_l = input('')
    input_l = input_l.replace(" ", "")
    mlist = input_l.split(",")

    letter1 = letters[mlist[0]]
    letter2 = letters[mlist[1]]
    total_dist = 0

    for i in range(letter1, letter2):
        tdist = bdist[keylist[i]]
        total_dist += tdist

    car = vehicle[mlist[2]]
    money = (float(total_dist)/float(car)) * float(mlist[4])

    road = roads[mlist[3]]
    time = float(total_dist*60)/float(road)
    hour = time//60
    min = time - hour*60

    output1.append(str(total_dist))
    output2.append(hour)
    output3.append(min)
    output4.append(money)

for i in range(0,5):
    print("%s, %02.0f:%02.0f, $%0.2f" % (output1[i], output2[i], output3[i], output4[i]))
