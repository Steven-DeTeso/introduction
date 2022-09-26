num1 = 42 #variable declaration #primative data type
num2 = 2.3 #variable declaration #primative data type 'float'
boolean = True #variable declaration, primative data type Boolean
string = 'Hello World' #variable declaration
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, an array
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration, a Class?
fruit = ('blueberry', 'strawberry', 'banana') #var declaration, List
print(type(fruit)) #print statement displaying fruit list
print(pizza_toppings[1]) #print statement displaying 'Sausage'
pizza_toppings.append('Mushrooms') # adding 'Mushrooms' to var pizza_toppings
print(person['name']) #print statment displaying 'John'
person['name'] = 'George' #changing persons name to 'George'
person['eye_color'] = 'blue' #adding persons eye_color 'blue'
print(fruit[2])

if num1 > 45: #conditional if
    print("It's greater")
else: #conditional else
    print("It's lower")

if len(string) < 5: #conditional if length of string less than 5
    print("It's a short word!")
elif len(string) > 15: #else if statement length of string greater than 15
    print("It's a long word!")
else: #conditional else
    print("Just right!")

for x in range(5): #for loop with a range of ? to 5
    print(x)
for x in range(2,5): #for loop with a range of 2 to 5
    print(x)
for x in range(2,10,3): #for loop, not sure range
    print(x)
x = 0 #var declaration x = 0
while(x < 5): #while loop to run while x is less than 5
    print(x)
    x += 1 # x = x + 1

pizza_toppings.pop() #removing last entry in pizza_toppings
pizza_toppings.pop(1) #removing second entry in pizza_toppings

print(person) 
person.pop('eye_color') #removing eye color and its value in person class
print(person)

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times(): #defining a function with a for loop that checks if a number is in range 10
    for num in range(10):
        print('Hello')

print_hello_ten_times() #calling the function

def print_hello_x_times(x): #defining function 
    for num in range(x):
        print('Hello')

print_hello_x_times(4) #calling function

def print_hello_x_or_ten_times(x = 10): #defining function and passing arguments
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)