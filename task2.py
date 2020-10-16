import random
# Defining functions
def generate_pos_int():
    """ Get two random positive integers """
    num1 = random.randint(1,9)
    num2 = random.randint(1,9)
    return (num1, num2)

def calculate_product(val1, val2):
    """Calculate the product of two numbers"""
    return val1 * val2
 
def main():
    """main function of the program"""
    num1, num2 = generate_pos_int()
    while True:
        input_product = int(input(f'How much is {num1} times {num2} '))
        random_product = calculate_product(num1,num2)
        if input_product == random_product:
            print('Done')
            break
        else:
            print(f'{num1} times {num2} is not {input_product}, please try again:')
    
# Start program
main()