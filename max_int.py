#The user inputs an integer until a negative number inentered. Algorithm findes
#the maximum positive number input.

num_int = int(input("Please input an integer: "))
num_max = 0

if num_int >= 0:
    while True:
        num_max = max(num_int)

elif num_int < 0:
