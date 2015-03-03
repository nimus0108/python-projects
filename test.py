# Get input
init_input =input("Enter our statement to be evaluated. ")
input_list = init_input.split()

# The loop should automatically continue the first time
should_continue = "y"

#While loop until user keeps saying 'y'
while should_continue=="y":
    # no error at first
    error = False
    zeroerror = False

    input_list = init_input.split()
    #converting into float
    num1 = float(input_list[0])
    op = (input_list[1])
    num2 = float(input_list[2])

    #Check to see what operation to perform
    if op=="+":
        result = num1+num2
    elif op =="-":
        result = num1 - num2
    elif op=="*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            zeroerror = True
        else:
            result = num1/num2
    else:
        error = True

    # Check for error
    if  (error==True):
        print("Error: Invalid operator")
    elif (zeroerror == True):
        print("Error: Division by zero")
    else:
        print("Result: " + str(result))

    # Should continue?
    should_continue = input("Would you like to perform another calculation? (y/n)")
    if should_continue=="y":
        init_input = input("Enter our statement to be evaluated. ")
    else:
        break

