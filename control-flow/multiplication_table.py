num = int(input("Enter a number to see its multiplication table:"))                   # prompting the user to enter a number for the multiplication number.
for i in range(1,11):
    result = i * num
    print(f"{num}*{i} = {result}")