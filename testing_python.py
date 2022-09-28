# import random

# print('Welcome to Python!')

# print('This is a loop printing 5 times')
# for x in range(1, 6):
#     print(f'x is: {x}')

# weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
# day = random.choice(weekdays)

# print(f'Today is: {day}')

# if day == 'Monday':
#     print('It will be a long week!')
# elif(day == 'Friday'):
#     print('Woohoo, time for the weekend!')
# else:
#     print('Not quite there yet.')

# some_nums = [44,56,2,3,12,19,6]
# print("Get started by writing your own code!")

# # Some optional challenges to assess and refine your understanding:

# # Print the length of the list.
# print(len(some_nums))

# # Use antoher python built-in function and print the result.
# print(some_nums.index(3))

# # Remove an item from the list. Remember to verify that it was removed.
# some_nums.pop()
# print(some_nums)

# Utilize a method from the documentation and print the result.


# for x in range(0, 10, 2):
#     print(x)
# # output: 0, 2, 4, 6, 8
# for x in range(5, 1, -3):
#     print(x)
# # output: 5, 2

# # Challenge: Write a for loop to print all integers from 1 to 20, including 20
# for x in range(1, 21):
#     print(x)

# countries = ["Uganda", "Chile", "Albania", "Saudi Arabia"]

# Challenge 1: Fix the range!
# for integer in range(0, len(countries)):
    # print(countries[integer])
    # Challenge 2: print the index here
    # print(countries)
    # Challenge 3: print the country here

# Looping over values only...
# for country in countries:
#     print(country)
    # Challenge 4: print the country here

# count = 0
# while count <= 5:
#     print("looping - ", count)
#     count += 1

y = 3
while y > 0:
    print(y)
    y = y - 1
    if y == 0:
        break
else:		# only executes on a clean exit from the while loop (i.e. not a break)
    print("Final else statement")