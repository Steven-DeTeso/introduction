# Print Sum 0-255
# Print the intergers from 0 to 255, and with each integer print the sum so far. 

# Define a function


def print_sum():
    # Creat a sum variable
    s = 0  
    # Interate through th erange of numbers
    for i in range(0, 256):
    # print each number 
        print(i)
        # add each number to the sum variable 
        s += i
    # print sum variable
        # print(s)

# print_sum()

# Find and Print Max
# Given a list, find and print its largest string

# Define a function that accepts a list
def find_and_print_max(list:list[str]) -> None:
    max_string = list[0]

    for a in list: 
        if len(a) > len(max_string):
            print(f'Value {a} is longer than value {max_string}')
            max_string:str = a

    print(max_string)

find_and_print_max(['Moore', 'Rene', 'Jonathan', 'Marino', 'Hello', 'World'])