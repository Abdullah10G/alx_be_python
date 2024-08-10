num_1 = int(input("Enter the first number:"))
num_2 = int(input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /):")

match operation :
    case "+":
        addition = num_1 + num_2
        print(f"The result is {addition}.")
    case "-":
        subsratction = num_1 - num_2
        print(f"The result is {subsratction}.")
    case "*":
        multipy = num_1 * num_2
        print(f"The result is {multipy}.")
    case "/":
        if num_2 == 0:
            print("You cannot divide by zero.")
        else:    
            divide = num_1 / num_2
            print(f"The result is {divide}.")
    case _:
        print("Operation isn't included , Try again.")