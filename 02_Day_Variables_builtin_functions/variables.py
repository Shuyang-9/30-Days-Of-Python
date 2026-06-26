
# Variables in Python

first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname': 'Asabeneh',
    'lastname': 'Yetayeh',
    'country': 'Finland',
    'city': 'Helsinki'
}

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

# 尝试

print('Hello, World!')
print('Hello',',', 'World','!')
print(len('Hello, World!'))

# first_name = input('What is your name: ')
# age = input('How old are you? ')
# print(first_name)
# print(age)

print(type(zip([1,2],[3,4])))    # zip

num_int = 10
print('num_int:',num_int)
num_float = float(num_int)
print('num_float:', num_float)

# str to int or float
num_str = '10.6'
num_float = float(num_str)  # Convert the string to a float first
num_int = int(num_float)    # Then convert the float to an integer
# print('num_int', int(num_str))      # 这一句有误， string 为带小数点的字符串，无法直接用 int() 转换。
print('num_float', float(num_str))  # 10.6
# num_int = int(num_float)  # 上面已写过
print('num_int', int(num_int))      # 10

num_str = '11'
num_int = int(num_str)
print('num_int:', num_int)

# str to list
first_name = 'Asabeneh'
print(first_name)               # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']



# Day 2: 30 Days of python programming

# Exercises: Level 1
first_name = 'Shuyang'
last_name = 'Shi'
full_name = 'Shuyang Shi'
country = 'China'
city = 'Changzhou'
age = 25
year = 2026
is_married = False
is_true = True
is_light_on = False
fruit, sport, color, number = 'apple', 'air rifle', 'red', 9

# Exercises: Level 2
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(fruit), type(sport), type(color), type(number))

print(len(first_name))
print(len(last_name))
print('Is first name longer than last name?', len(first_name) > len(last_name))  # 比较两者长度

num_one = 5
num_two = 4

total = num_one + num_two
print('total:', total)

diff = num_one - num_two
print('diff:', diff)

product = num_one * num_two
print('product:', product)

division = num_one / num_two
print('division:', division)

remainder = num_two % num_one
print('remainder:', remainder)

exp = num_one ** num_two
print('exp:', exp)

floor_division = num_one // num_two
print('floor_division:', floor_division)

pi = 3.14
# radius = 30
radius = float(input('radius = '))  # 注意**不支持int和float同时计算，需要在输入时int to float
area_of_circle = pi * radius ** 2
circum_of_circle = 2 * pi * radius
print('area_of_circle', area_of_circle)
print('circum_of_circle', circum_of_circle)

first_name_user = input('What is your first name: ')
last_name_user = input('What is your last name: ')
country_user = input('Where are you from: ')
age_user = input('How old are you: ')
print(first_name_user, last_name_user, country_user, age_user)

help('keywords')
