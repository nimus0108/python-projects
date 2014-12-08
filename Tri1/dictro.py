

test_dict = {}

test_dict["yankees"] = 80
test_dict["red sox"] = 50
test_dict["blue jays"] = 45

key_lists = list(test_dict.keys())

key_lists.sort()

for team in key_lists:
    print(team + " won", test_dict[team], "games.")
