import math
import sys 

print("Welcome")

a = int(input("Enter your number: "))

if a < 0: 
    print("please enter a positive number") 
    sys.exit()


else: 
    b = math.sqrt(a)
    print("The answer is:" , (b))
    
    
    
# feel free to edit or reuse
