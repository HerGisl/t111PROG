#The user inputs an integer until a negative number inentered. Algorithm findes
#the maximum positive number input.

num_int = int(input("Please input an integer: "))
num_max = 0

while num_int >= 0:
    if num_int > num_max:
        num_max = num_int
        num_int = int(input("Please input an integer: "))
    
        

print(num_max)