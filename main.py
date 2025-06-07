import math 
import sys 

print("Welcome")

a = float(input("Enter your number: "))    

if a < 0: 
    print("please enter a positive number")        #only positive numbers 
    sys.exit()


else: 
    b = math.sqrt(a)
    print("The answer is:" , (b))                # the answer
    
    
    
# feel free to edit or reuse
