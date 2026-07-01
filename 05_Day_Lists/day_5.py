empty_list = list()  # this is an empty list, no item in the list
print(len(empty_list))  # 0

# list of fruits
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage',
              'Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter',
                   'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React', 'Redux',
             'Node', 'MongDB']  # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# Print the lists and it length
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:', animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Number of countries:', len(countries))

# Modifying list

fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0]  # we are accessing the first item using its index
print(first_fruit)      # banana
second_fruit = fruits[1]
print(second_fruit)     # orange
last_fruit = fruits[3]
print(last_fruit)  # lemon
# Last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]

# Accessing itmes
fruits = ['banana', 'orange', 'mango', 'lemon']
last_fruit = fruits[-1]
second_last = fruits[-2]
print(last_fruit)       # lemon
print(second_last)      # mango

# Slicing items
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4]  # it returns all the fruits
# this is also give the same result as the above
all_fruits = fruits[0:]  # if we don't set where to stop it takes all the rest
orange_and_mango = fruits[1:3]  # it does not include the end index
orange_mango_lemon = fruits[1:]
banana_and_mango = fruits[::2]
print(banana_and_mango)
orange_and_lemon = fruits[1::2]
print(orange_and_lemon)

fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:]  # it returns all the fruits
# this is also give the same result as the above
orange_and_mango = fruits[-3:-1]  # it does not include the end index
orange_mango_lemon = fruits[-3:]


fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'Avocado'
print(fruits)  # ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'apple'
print(fruits)  # ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits)
fruits[last_index - 1] = 'lime'
print(fruits)  # ['avocado', 'apple', 'mango', 'lime']

# checking items
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False

# Append
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']
# ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime]
fruits.append('lime')
print(fruits)

# insert
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple')  # insert apple between orange and mango
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
# ['banana', 'orange', 'apple', 'mango', 'lime','lemon',]
fruits.insert(4, 'lime')
print(fruits)

# remove
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon']
fruits.remove('lemon')
print(fruits)  # ['orange', 'mango']

# pop
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)       # ['banana', 'orange', 'mango']

fruits.pop(0)
print(fruits)       # ['orange', 'mango']

# del
fruits = ['banana', 'orange', 'mango', 'lemon']
del fruits[0]
print(fruits)       # ['orange', 'mango', 'lemon']

del fruits[1]
print(fruits)       # ['orange', 'lemon']
del fruits
# print(fruits)       # This should give: NameError: name 'fruits' is not defined

# clear
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)       # []

# copying a lits

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']

# join
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5, -4, -3, -2, -1]
integers = negative_numbers + zero + positive_numbers
print(integers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

# join with extend
num1 = [0, 1, 2, 3]
num2 = [4, 5, 6]
num1.extend(num2)
print('Numbers:', num1)
negative_numbers = [-5, -4, -3, -2, -1]
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits.extend(vegetables)
print('Fruits and vegetables:', fruits)

# count
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           # 3

# index
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))  # 2

# Reverse
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits)
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages)

# sort
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
ages.sort(reverse=True)
print(ages)

fruits_ed = sorted(fruits)
print(fruits)
print(fruits_ed)



# Exercises: Day 5
print('Exercises: Level 1')
print('\n# 1')
lst = []
print(lst)

print('\n# 2')
lst = [0, 1, 2, 3, 4, 5, 6]
print(lst)

print('\n# 3')
print(len(lst))

print('\n# 4')
first_item = lst[0]
middle_item = lst[int((len(lst) - 1) / 2)]  # 可以使用 lst[len(lst) // 2]
last_item = lst[-1]
print(first_item, middle_item, last_item)

print('\n# 5')
mixed_data_types = ['shisy', 25, 170, 'no', 'Yutian']
print(mixed_data_types)

print('\n# 6')
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

print('\n# 7')
print(it_companies)

print('\n# 8')
print(len(it_companies))

print('\n# 9')
print(it_companies[0])
print(it_companies[len(it_companies) // 2])
print(it_companies[-1])

print('\n# 10')
it_companies[0] = 'facebook0'
print(it_companies)

print('\n# 11')
it_companies.append('Ig')
print(it_companies)

print('\n# 12')
it_companies.insert(4, 'Meta')
print(it_companies)

print('\n# 13')
it_companies[1] = it_companies[1].upper()
print(it_companies)

print('\n# 14')
sentence = '#; '.join(it_companies)
print(sentence)

print('\n# 15')
does_exist = 'IBM' in it_companies
print(does_exist)

print('\n# 16')
it_companies.sort()
print(it_companies)

print('\n# 17')
it_companies.reverse()
print(it_companies)

print('\n# 18')
print(it_companies[:3])

print('\n# 19')
print(it_companies[-3:])

print('\n# 20')
middle_num = int(len(it_companies) // 2)
print(it_companies[4])

# 兼容奇数和偶数的写法
# middle = len(it_companies) // 2
# if len(it_companies) % 2 == 0:
#     print(it_companies[middle - 1:middle + 1])
# else:
#     print(it_companies[middle])

print('\n# 21')
del it_companies[0]
print(it_companies)

print('\n# 22')
del it_companies[3:5]
print(it_companies)

print('\n# 23')
del it_companies[-1]
print(it_companies)

print('\n# 24')
del it_companies[0:]
print(it_companies)

print('\n# 25')
del it_companies
# print(it_companies)

print('\n# 26')
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
lst_join = front_end + back_end
print(lst_join)

print('\n# 27')
full_stack = lst_join.copy()
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)

print('\nExercises: Level 2')
print('\n# 1')
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
min_age = ages[0]
max_age = ages[-1]
print('The min age is ', min_age)
print('The max age is ', max_age)
ages.insert(0, ages[0])
ages.append(ages[-1])
print(ages)
median_age = (ages[5] + ages[6]) / 2
print('The median age is ', median_age)
average_age = sum(ages) / len(ages)
print('The average age is ', average_age)
range_age = ages[-1] - ages[0]
print(range_age)
print('The value of (min - average) is larger than the value of (max - average): ', abs(min_age - average_age) > abs(max_age - average_age))

print('\n# 2')
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from data.countries import countries

# 上面的内容为连接到data文件夹中的countries.py文件

print(len(countries))
middle_country = countries[len(countries) // 2]
print(middle_country)
middle_num = int((len(countries) + 1) / 2)
first_list = countries[:middle_num]
second_list = countries[middle_num:]
print(len(first_list))
print(len(second_list))
CH, RU, US, *scandic_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(CH, RU, US, scandic_countries)

