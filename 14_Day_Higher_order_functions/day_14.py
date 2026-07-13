def decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@decorator
def hello():
    print("Hello")

hello()

# Applying Multiple Decorators to a Single Function
'''These decorator functions are higher order functions
that take functions as parameters'''

# First Decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Second decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper

#Decorators will be executed from bottom to top
@split_string_decorator
@uppercase_decorator     # order with decorators is important in this case - .upper() function does not work with lists
def greeting():
    return 'Welcome to Python'
print(greeting())   # ['WELCOME', 'TO', 'PYTHON']

# Accepting Parameters in Decorator Functions
def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(first_name, last_name))

print_full_name("Asabeneh", "Yetayeh",'Finland')

# python - map function
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # 可迭代对象

def change_to_upper(name):
    return name.upper()

names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']

# 让我们应用lambda函数
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']


# filter function
# 让我们只过滤偶数
numbers = [1, 2, 3, 4, 5]  # 可迭代对象

def is_even(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers))       # [2, 4]

# reduce function
from functools import reduce
numbers_str = ['1', '2', '3', '4', '5']  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)    # 15



# Exercises: Day 14
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Exercises: Level 1
print('\nExercises: Level 1')
print('# 1')

print('# 2')

print('# 3')

print('\n# 4')
for country in countries:
    print(country)


print('\n# 5')
for name in names:
    print(name)


print('\n# 6')
for number in numbers:
    print(number)


print('\nExercises: Level 2')
print('\n# 1')
def change_country_to_upper(country):
    return country.upper()
countries_upper = map(change_country_to_upper, countries)
print(list(countries_upper))


print('\n# 2')
def square(number):
    return number ** 2
numbers_square = map(square, numbers)
print(list(numbers_square))


print('\n# 3')
def change_name_to_upper(name):
    return name.upper()
names_upper = map(change_name_to_upper, names)
print(list(names_upper))


print('\n# 4')
def land_country(country):
    if 'land' in country:
        return True
    return False
countries_containing_land = filter(land_country, countries)
print(list(countries_containing_land))


print('\n# 5')
def country_name_six(country):
    if len(country) == 6:
        return True
    return False
country_name = filter(country_name_six, countries)
print(list(country_name))


print('\n# 6')
def country_name_morethansix(country):
    if len(country) >= 6:
        return True
    return False
country_name = filter(country_name_morethansix, countries)
print(list(country_name))


print('\n# 7')
def country_name_e(country):
    if country.startswith('E'):
        return True
    return False
country_name = filter(country_name_e, countries)
print(list(country_name))


print('\n# 8')
# 解答
from functools import reduce
result = reduce(lambda x, y: x + y, filter(lambda x: x > 20, map(lambda x: x ** 2, numbers)))
print(result)


print('\n# 9')
# 错误。不是把每个元素都转成string
# def get_string_lists(item):
#     item = str(item)
#     return item
def is_string(item):
    return type(item) == str
def get_string_lists(items):
    return list(filter(is_string, items))
# 或者
def get_string_lists(items):
    return list(filter(lambda item: type(item) == str, items))
# 或者
def get_string_lists(items):
    return [item for item in items if type(item) == str]

mixed_list = [1, 'Python', 3.5, 'SQL', True, 'GIS']
print(get_string_lists(mixed_list))


print('\n# 10')
def add_two_nums(x, y):
    total = x + y
    return total
sum_all_numbers = reduce(add_two_nums, numbers)
print(sum_all_numbers)


print('\n# 11')
# 最后两个国家之间缺少 and
# def country_name(a, b):
#     return a + ', ' + b
# country_list = reduce(country_name, countries)
# print(f'{country_list} are north European countries.')
countries_without_last = reduce(lambda a, b: a + ', ' + b, countries)
sentence = countries_without_last + ', and ' + countries[-1] + ' are north European countries.'
print(sentence)


print('\n# 12')
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1] / "data"))
from countries import countries as countries_data
# 写法不合题意，不是仅筛选出含有land的国家
# def categorize_countries(country):
#     if 'land' in country:
#         return True
#     return False
# country_list = filter(categorize_countries, countries_data)
# print(list(country_list))
# 函数应该接收两个参数
def categorize_countries(countries, pattern):
    return list(filter(lambda country: pattern.lower() in country.lower(), countries))
print(categorize_countries(countries_data, 'land'))
print(categorize_countries(countries_data, 'island'))
print(categorize_countries(countries_data, 'ia'))
print(categorize_countries(countries_data, 'stan'))


print('\n# 13')
# 错误
# country_first_letter = []
# for country in countries_data:
#     count = 0
#     if country[0] in country_first_letter:
#         count += 1
#     else:
#         country_first_letter.append(country[0])
#         count = 1
# print(country_first_letter)
# print(count)
def count_countries_by_first_letter(countries):
    result = {}
    for country in countries:
        first_letter = country[0].upper()
        if first_letter in result:
            result[first_letter] += 1
        else:
            result[first_letter] = 1
    return result
country_counts = count_countries_by_first_letter(countries_data)
print(country_counts)


print('\n# 14')
def get_first_ten_countries(countries):
    return countries[:10]
print(get_first_ten_countries(countries_data))

print('\n# 15')
def get_last_ten_countries(countries):
    return countries[-10:]
print(get_last_ten_countries(countries_data))


print('\nExercises: Level 3')
print('\n# 1')
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1] / "data"))
from countries_data import countries_data as countries_data_data
# 按国家名称排序
countries_by_name = sorted(countries_data_data, key=lambda country: country['name'])
for country in countries_by_name:
    print(country['name'])

# 按首都排序
countries_by_capital = sorted(countries_data_data, key=lambda country: country['capital'])
for country in countries_by_capital:
    print(country['name'], country['capital'])

# 按人口排序
countries_by_population = sorted(countries_data_data, key=lambda country: country['population'], reverse=True)
for country in countries_by_population:
    print(country['name'], country['population'])

# 统计每种语言出现在多少国家中，找出前十名
language_counts = {}
for country in countries_data_data:
    for language in country['languages']:
        if language in language_counts:
            language_counts[language] += 1
        else:
            language_counts[language] = 1
language_counts_list = list(language_counts.items())
language_counts_list.sort(key=lambda item: item[1], reverse=True)
print(language_counts_list[:10])

# 统计前十名人口最多的国家
countries_by_population = sorted(countries_data_data, key=lambda country: country['population'], reverse=True)
top_ten_population = countries_by_population[:10]
for country in top_ten_population:
    print(country['name'], country['population'])