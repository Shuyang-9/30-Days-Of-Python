# Arithmetic Operations in Python
# Integers

print('Addition: ', 1 + 2)
print('Subtraction: ', 2 - 1)
print('Multiplication: ', 2 * 3)
# Division in python gives floating number
print('Division: ', 4 / 2)
print('Division: ', 6 / 2)
print('Division: ', 7 / 2)
# gives without the floating number or without the remaining
print('Division without the remainder: ', 7 // 2)
print('Modulus: ', 3 % 2)                           # Gives the remainder
print('Division without the remainder: ', 7 // 3)
print('Exponential: ', 3 ** 2)                     # it means 3 * 3

# Floating numbers
print('Floating Number,PI', 3.14)
print('Floating Number, gravity', 9.81)

# Complex numbers
print('Complex number: ', 1+1j)
print('Multiplying complex number: ', (1+1j) * (1-1j))  # 答案为 (2+0j) 因为在 Python 里，只要参与运算的是复数 complex，结果就会保持为复数类型。
result = (1+1j) * (1-1j)
print(result.real)  # 如果想只输出实部

# Declaring the variable at the top first

a = 3  # a is a variable name and 3 is an integer data type
b = 2  # b is a variable name and 3 is an integer data type

# Arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# I should have used sum instead of total but sum is a built-in function try to avoid overriding builtin functions
print(total)  # if you don't label your print with some string, you never know from where is  the result is coming
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

# Declaring values and organizing them together
num_one = 3
num_two = 4

# Arithmetic operations
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_two
remainder = num_two % num_one

# Printing values with label
print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)


# Calculating area of a circle
radius = 10                                 # radius of a circle
# two * sign means exponent or power
area_of_circle = 3.14 * radius ** 2
print('Area of a circle:', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')

# Calculate the density of a liquid
mass = 75 # in Kg
volume = 0.075 # in cubic meter
density = mass / volume # 1000 Kg/m^3
print(density, 'Kg/m^3') # Adding unit to the density

print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False

# Boolean comparison
print('True == True: ', True == True)       # True
print('True == False: ', True == False)     # False
print('False == False:', False == False)    # True
print('True and True: ', True and True)     # True
print('True or False:', True or False)      # True
print('True and False: ', True and False)   # False
print('False and False: ', False and False) # False

# Another way comparison
# True - because the data values are the same
print('1 is 1', 1 is 1)                    # True - because 1 is 1
print('1 is not 2', 1 is not 2)            # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh')  # True - A found in the string
print('B in Asabeneh', 'B' in 'Asabeneh')  # False -there is no uppercase B
print('coding' in 'coding for all')        # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')       # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

print(3 > 2 and 4 > 3)  # True - because both statements are true
print(3 > 2 and 4 < 3)  # False - because the second statement is false
print(3 < 2 and 4 < 3)  # False - because both statements are false
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statement is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False)  # False



# Day 3
# Exercises
age = 25

height = 170.5

question = 1 + 2j

base = float(input('Enter base: '))
height = float(input('Enter height: '))
area = int(0.5 * base * height)
print('The area of the triangle is ', area)

a = int(input('Enter side a: '))
b = int(input('Enter side b: '))
c = int(input('Enter side c: '))
perimeter = a + b + c
print('The perimeter of the triangle is ', perimeter)

length = int(input('Enter length: '))
width = int(input('Enter width: '))
area = length * width
perimeter = 2 * (length + width)
print('The perimeter of the rectangle is ', perimeter)
print('The area of the rectangle is ', area)

pi = 3.14
radius = float(input('Enter radius: '))
area = pi * radius ** 2
circumference = 2 * pi * radius
print('The circumference of the circle is ', circumference)
print('The area of the circle is ', area)

y1 = 0
x1 = (y1 + 2) / 2
x2 = 0
y2 = 2 * x2 - 2
slope_8 = (y2 - y1) / (x2 - x1)
print('x-intercept: ', x1)
print('y-intercept: ', y2)
print('slope: ', slope_8)
# 可以直接写 slope_8 = 2 因为原方程是斜截式

x1, y1 = 2, 2
x2, y2 = 6, 10
slope_9 = (y2 - y1) / (x2 - x1)
distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
print('slope: ', slope_9)
print('distance: ', distance)

print('slope in task 8 equals to slope in task 9', slope_8 == slope_9)

# task 11
x = int(input('Enter the value of x to let y be 0: '))  # 可以直接写 x = -3
y = x ** 2 + 6 * x + 9
print('The value of y is: ', y)

# task 12
print(len('python') == len('dragon'))
# 改成 print(len('python') != len('dragon')) 输出 False 因为题干要求 False的比较语句

# task 13
print('on' in 'python' and 'on' in 'dragon')

# 14
print('jargon' in 'I hope this course is not full of jargon')

# 15
print('on' not in 'dragon' and 'on' not in 'python')

# 16
length = len('python')
length_float = float(length)
length_string = str(length_float)
print('length_float: ', length_float)
print('length_string: ', length_string)

# 17
number = int(input('The number is: '))
print('The number is even.', number % 2 == 0)

# 18
print('The floor division of 7 by 3 is equal to the int converted value of 2.7.', 7 // 3 == int(2.7))

# 19
print("type of '10' is equal to type of 10.", type('10') == type(10))

# 20
number = '9.8'
number = float(number)
number = int(number)
print("int('9.8') is equal to 10.", number == 10)
# 写成 print(int(float('9.8')) == 10) 避免报错，输出 False

# 21
hours = int(input('Enter hours: '))
rate_per_hour = int(input('Enter rate per hour: '))
earning = hours * rate_per_hour
print('Your weekly earning is ', earning)

# 22
years = int(input('Enter number of years you have lived: '))
seconds = years * 31536000
print('You have lived for ', seconds, 'seconds')

# 23
print(
    '''
    1 1 1 1 1
    2 1 2 4 8
    3 1 3 9 27
    4 1 4 16 64
    5 1 5 25 125
    '''
)

