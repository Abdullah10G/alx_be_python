size = int(input("Enter the size of the pattern:"))                 # prompting the user to enter the size of the pattern.
i = 1
while i <= size:   
    for j in range(0,size):
        print("*", end="")
    i += 1         
    print()
       