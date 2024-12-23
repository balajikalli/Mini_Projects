"""
/ - division
+  - addition 
-  - subtraction
*  - multiplication
% - remainder
** - power

"""
# WHILE LOOP is just because, if we accidentally enter operand2 string, loop will go back to ask "enter operand2."
#If we add operand2 correct as number, then it will take it and break WHILE LOOP.

# WE CALL FUNCTION, so that we can call MULTIPLE TIMES.

def get_numbers(number):
    while True:
        operand1 = input("Enter Number " + str(number) + ":")
        try:
            return float(operand1)
        except:
            print("Invalid Number, Try Again..!")
    
operand1 = get_numbers(1)
operand2 = get_numbers(2)
operator = input("Enter Sign: ")

#THIS TRY AND EXCEPT blocks are help the code, in TRY we are changing everything into floats. 
# Numbers like integers can change into Float. if we add any characters, it will go to EXCEPT BLOCK and print invalid...

try:
    operand1 = float(operand1)
    operand2 = float(operand2)

    if operator == "+":
        result = (operand1) + (operand2)
        print("The result is: ", result) 

    elif operator == "-":
        result = (operand1) - (operand2)
        print("The result is: ", result)

    elif operator == "/":
        if (operand2) != 0:
            result = (operand1) / (operand2)
            print("The result is: ", result)

        else:
            print("Division by Zero")

    elif operator == "*":
        result = (operand1) * (operand2)
        print("The result is: ", result)

    elif operator == "%":
        result = (operand1) % (operand2)
        print("The result is: ", result)

    elif operator == "**":
        result = (operand1) ** (operand2)
        print("The result is: ", result)

    else:
        print("Undefined Numbers...")


except:
    print("Invalid Numbers.")