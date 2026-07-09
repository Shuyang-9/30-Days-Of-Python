def greetings (name):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings('Asabeneh'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))


def greetings (name = 'Peter'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Asabeneh'))

def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i)
print(generate_groups('Team-1','Asabeneh','Brook','David','Eyob'))

# dictionary unpacking
# Define a function that takes two arguments: 'name' and 'location'
def greet(name, location):
    # Print a greeting message using the provided arguments
    print("Hi there", name, "how is the weather in", location)

# Call the function using keyword arguments
greet(name="Alice", location="New York")
# Output: Hi there Alice how is the weather in New York

# Create a dictionary with keys matching the function's parameter names
my_dict = {"name": "Alice", "location": "New York"}

# Call the function using dictionary unpacking
greet(**my_dict)
# The ** operator unpacks the dictionary, passing its key-value pairs
# as keyword arguments to the function.
# Output: Hi there Alice how is the weather in New York


#You can pass functions around as parameters
def square_number (n):
    return n ** n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) # 27



# Exercises: Day 11
# Exercises: Level 1
print('\nExercises: Level 1')
print('\n# 1')
def add_two_numbers(x, y):
    return x + y

print('\n# 2')
def area_of_circle(r):
    pi = 3.14
    area = pi * r * r
    return area

print('\n# 3')
def add_all_nums(*nums):
    total = 0
    for num in nums:
        if type(num) == int or type(num) == float:  # 注意数字类型有两种
            print(f'{num} is a number')
            total += num
        else:
            print(f'{num} is {type(num)}')
    return total
print(add_all_nums(1,2,3,'xx'))

print('\n# 4')
def convert_celsius_to_fahrenheit(c_value):
    f_value = (c_value * 9 / 5) + 32
    return f_value

print('\n# 5')
def check_season(month):
    if month in ['September', 'October', 'November']:
        return 'Autumn'
    elif month in ['December', 'January', 'February']:
        return 'Winter'
    elif month in ['March', 'April', 'May']:
        return 'Spring'
    elif month in ['June', 'July', 'August']:
        return 'Summer'

print('\n# 6')
# def calculate_slope(y = a * x + b):  # 报错 name 'a' is not defined
#     return a
# print(calculate_slope(y = 2 * x + 1))
def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

print('\n# 7')
def solve_quadratic_eqn(a, b, c):  # 注意区分delta的值
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        x1 = (- b + delta ** 0.5) / (2 * a)
        x2 = (- b - delta ** 0.5) / (2 * a)
        # return (- b + delta ** 0.5) / (2 * a) and (- b - delta ** 0.5) / (2 * a)  # 这样写只会返回最后一个值
        return x1, x2
    if delta == 0:
        return - b / (2 * a)
    else:
        return "No solution"
print(solve_quadratic_eqn(1, -9, 18))

print('\n# 8')
def print_list(lst):
    for item in lst:
        print(item)  # 注意不能用 return，否则循环一次就结束了

print('\n# 9')
def reverse_list(lst):
    lst_reverse = []
    for i in range(len(lst)-1, -1, -1):
        lst_reverse.append(lst[i])
    return lst_reverse
print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]))

print('\n# 10')
def capitalize_list_items(lst):
    lst_capitalize = []
    for item in lst:
        lst_capitalize.append(item.capitalize())
    return lst_capitalize
print(capitalize_list_items(['aa', 'bbb', 'cccc']))

print('\n# 11')
def add_item(lst, item):
    lst.append(item)
    return lst
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_stuff, 'Meat'))
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))
# 可以复制 lst 再进行操作，不改变原来的列表

print('\n# 12')
def remove_item(lst, item):
    lst.remove(item)
    return lst
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff, 'Mango'))
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))
# 可以复制 lst 再进行操作，不改变原来的列表

print('\n# 13')
def sum_of_numbers(number):
    total = 0
    for i in range(number + 1):
        total += i
    return total
print(sum_of_numbers(5))
print(sum_of_numbers(10))
print(sum_of_numbers(100))

print('\n# 14')
def sum_of_odds(number):
    total = 0
    for i in range(number + 1):
        if i % 2 == 1:
            total += i
    return total
print(sum_of_odds(5))

print('\n# 15')
def sum_of_even(number):
    total = 0
    for i in range(number + 1):
        if i % 2 == 0:
            total += i
    return total
print(sum_of_even(5))


# Exercises: Level 2
print('\nExercises: Level 2')
print('\n# 1')
def evens_and_odds(number):
    even_number = 0
    odd_number = 0
    if number > 0:
        if number % 2 == 0:
            even_number = int(number / 2 + 1)
            odd_number = int(number / 2)
        if number % 2 == 1:
            even_number = int((number + 1) / 2)
            odd_number = int((number + 1) / 2)
        return f"The number of odds are {odd_number}.\nThe number of evens are {even_number}."
    else:
        return "The number is not a positive number."
print(evens_and_odds(100))

# 下面为更通用的写法
# def evens_and_odds(number):
#     even_count = 0
#     odd_count = 0

#     for i in range(number + 1):
#         if i % 2 == 0:
#             even_count += 1
#         else:
#             odd_count += 1

#     return f"The number of odds are {odd_count}.\nThe number of evens are {even_count}."

print('\n# 2')
def factorial(number):
    total = 1
    for i in range(number, 0, -1):
        total *= i
    return total

print('\n# 3')
def is_empty(a):
    if len(a) > 0:
        return "It is not empty."
    else:
        return "It is empty."

# 下面为考虑数字的写法
# def is_empty(value):
#     if type(value) == int or type(value) == float:
#         return False
#         if len(value) == 0:
#         return True
#     else:
#         return False

# 更简洁一点
# def is_empty(value):
#     if type(value) == int or type(value) == float:
#         return False
#     return len(value) == 0

print('\n# 4')
def calculate_mean(lst):
    total_num = 0
    for item in lst:
        total_num += item
    return total_num / len(lst)

# 用 sum 的简单函数
# def calculate_mean(lst):
#     return sum(lst) / len(lst)

# 中位数计算选取最中间的值，区分数量奇偶
def calculate_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    if n % 2 == 1:
        return sorted_lst[n // 2]
    else:
        middle1 = sorted_lst[n // 2 - 1]
        middle2 = sorted_lst[n // 2]
        return (middle1 + middle2) / 2

# 计算众数
def calculate_mode(lst):
    max_count = 0
    mode_value = None
    for item in lst:
        count = lst.count(item)
        if count > max_count:
            max_count = count
            mode_value = item
    return mode_value

# 计算最大最小值范围
def calculate_range(lst):
    return max(lst) - min(lst)

# 计算方差
def calculate_variance(lst):
    mean = calculate_mean(lst)  # 使用前面的计算平均值函数
    total = 0
    for item in lst:
        total += (item - mean) ** 2
    return total / len(lst)

# 计算标准差
def calculate_std(lst):
    return calculate_variance(lst) ** 0.5  # 使用前面的计算方差函数



print('\n# 5')
def greet(name = "Guest"):
    print(f"Hello, {name}!")
greet()
greet("Alice")

print('\n# 6')
# 错误
# def show_args(*args):
#     print(f"Received: name: {name}, age: {age}, city: {city}, pet: {pet}")
# show_args(name="Alice", age=30, city="New York")
# show_args(name="Bob", pet="Fluffy, the bunny")

# 用 ** 表示接收任意数量的带名字的参数

def show_args(**args):
    print("Received:", end=" ")
    for key, value in args.items():
        print(f"{key}: {value}", end=", ")
    print()
show_args(name="Alice", age=30, city="New York")
show_args(name="Bob", pet="Fluffy, the bunny")

# Exercises: Level 3
print('\nExercises: Level 3')
print('\n# 1')
# 判断是否为质数
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
print(is_prime(2))

def is_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number > 2:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True

print('\n# 2')
def unique_list(lst):
    if len(lst) == len(set(lst)):  # 注意 set 中的值唯一
        print('All items are unique in the list.')
    else:
        print('Not unique')

# 可以简化
def unique_list(lst):
    return len(lst) == len(set(lst))

print('\n# 3')
# 错误，现在每比较一组就会print一次
# def same_data_type(lst):
#     for i in range(len(lst)-1):
#         if type(lst[i]) == type(lst[i + 1]):
#             print('All the items of the list are of the same data type.')
#         else:
#             print('Not the same')

def same_data_type(lst):
    first_type = type(lst[0])
    for item in lst:
        if type(item) != first_type:
            return False
    return True
print(same_data_type([1, 1, 3]))
print(same_data_type([1, 2, 5, 'a']))

print('\n# 4')
# isidentifier 用法
def valid_variable(variable):
    return variable.isidentifier()

print('\n# 5')
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "data"))

from countries_data import countries_data

def most_spoken_languages(n=10):
    language_count = {}
    for country in countries_data:
        for language in country["languages"]:
            if language in language_count:
                language_count[language] += 1
            else:
                language_count[language] = 1
    language_count_list = list(language_count.items())
    language_count_list.sort(key=lambda i:i[1], reverse=True)
    return language_count_list[:10]
print(most_spoken_languages())

def most_populated_countries(n=10):
    population_list = []
    for country in countries_data:
        population_list.append((country['name'], country['population']))
    population_list.sort(key=lambda i:i[1], reverse=True)
    return population_list[:10]
print(most_populated_countries())