
init_input = input("Enter our statement to be evaluated. ")
should_continue = "y"
error = False

#while (should_continue == "y"):
input_list = init_input.spilt()
num1 = input_list[0]
op = input_list[1]
num2 = input_list[2]

if op=="+":
    result = num1+num2
elif op =="-":
    result = num1 - num2
elif op=="*":
    result = num1 * num2
elif op == "/":
    result = num1/num2
else:
    error = True

if error==True:
    print("Error: invalid operator")
else:
    print("Result: " + result)
print("Result: " + result)
should_continue = input("Would you like to perform another calculation? (y/n)")
