language = 'python'
lst = list(language)
print(lst)

def power(x):
    return lambda n: x ** n

cube = power(2)(3)   # 函数 power 现在需要两个单独的括号中的参数
print(cube)          # 8
two_power_of_five = power(2)(5)
print(two_power_of_five)  # 32

# Exercises: Day 13
print('\n# 1')
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_zero_numbers = [n for n in numbers if n <= 0]
print(negative_zero_numbers)


print('\n# 2')
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [n for row in list_of_lists for n in row]
print(flattened_list)


print('\n# 3')
# def power(x):
#     for n in range(6):
#         power_result = lambda x: x ** n
#     return power_result
# lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list_of_tuples = [(a, power(a)) for a in lst]
# print(list_of_tuples)
list_of_tuples = [(x, ) + tuple(x ** n for n in range(6)) for x in range(11)]
print(list_of_tuples)


print('\n# 4')
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# 方法一
flattened_countries = []
for item in countries:
    country, capital = item[0]
    flattened_countries.append([country.upper(), country[:3].upper(), capital.upper()])
print(flattened_countries)

# 方法二
flattened_countries = [[country.upper(), country[:3].upper(), capital.upper()] for item in countries for country, capital in item]
print(flattened_countries)


print('\n# 5')
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
new_list = [{'country': country.upper(), 'city': capital.upper()} for item in countries for country, capital in item]
print(new_list)

print('\n# 6')
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
new_list = [first_name + ' ' + last_name for item in names for first_name, last_name in item]
print(new_list)


print('\n# 7')
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
y_intercept = lambda x1, y1, x2, y2: (y1 - slope(x1, y1, x2, y2) * x1)
print(slope(1, 1, 0, -1))
print(y_intercept(1, 1, 0, -1))