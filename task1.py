import random
#constants
MIN = 1
MAX = 100

#defining functions
def is_prime(number):
    """ Calculate if the number is prime"""
    flag = False
    if number == 1:
        flag = False
    elif number ==2:
        flag = True
    else:        
        for j in range(2,number):
            if (number % j) == 0:
                flag = False
                break
            else:
                flag = True
    return flag                 

#start of main program
for i in range(1,7):
    num = random.randint(MIN,MAX)
    if(is_prime(num) == True):
        print(f'The random number {num} is a prime number.')
    else:
        print(f'The random number {num} is not a prime number.')        
    


