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
def find_and_print_max(list):
    # This function is designed to find the longest string in a provided list

        #Expects as an input: a list of strigs

        # This function does not return anything, but only prints the longest string
        
    # Set a max variable to track the largest string
    max_string = list[0]
    # iterate through the list with a for loop
    for a in list:
        # compare each value to the max variable
        if len(a) > len(max_string):
            print(f'Value {a} is longer than value {max_string}')
            max_string = a
            # if so, set max to be the current value
        # print max variable
        print(max_string)

find_and_print_max(['Moore', 'Rene', 'Jonathan', 'Marino', 'Hello', 'World'])