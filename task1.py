import random
#constants
MIN = 1
MAX = 100

#defining functions
def is_prime(number):
    """ Calculate the number is prime"""
    flag = 0
    if number > 1:
        for j in range(2,number//2):
            if (number % j) == 0:
                flag = 1
                break  

        if flag == 1:
            print(f'The random number {num} is not a prime number.')
        else:
            print(f'The random number {num} is a prime number.')          
    else:
        print(f'The random number {number} is not a prime number.')

#start of main program
for i in range(1,7):
    num = random.randint(MIN,MAX)
    is_prime(num)
    


