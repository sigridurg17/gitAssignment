num_int = 0
max_int = 0

num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code
# Do not change this line


while num_int >=0:
    num_int = int(input("Input a number: "))
    if num_int > max_int:
        max_int = num_int
    else:
        break
print("The maximum is", max_int)