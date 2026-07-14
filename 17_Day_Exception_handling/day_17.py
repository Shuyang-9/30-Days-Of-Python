# try:
#     print(10 + '5')
# except:
#     print('出现了一些错误')


# try:
#     name = input('输入你的名字:')
#     year_born = input('你出生的年份:')
#     age = 2026 - year_born
#     print(f'你是{name}. 你的年龄是{age}.')
# except:
#     print('出现了一些错误')


# try:
#     name = input('输入你的名字:')
#     year_born = input('你出生的年份:')
#     age = 2019 - int(year_born)
#     print(f'你是{name}. 你的年龄是{age}.')
# except TypeError:
#     print('发生了类型错误')
# except ValueError:
#     print('发生了值错误')
# except ZeroDivisionError:
#     print('发生了除零错误')
# else:
#     print('我通常与try块一起运行')
# finally:
#     print('我总是运行。')


# try:
#     name = input('输入你的名字:')
#     year_born = input('你出生的年份:')
#     age = 2019 - year_born
#     print(f'你是{name}. 你的年龄是{age}.')
# except Exception as e:
#     print(e)


def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e
lst = [1, 2, 3, 4, 5]
# print(sum_of_five_nums(lst)) # TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'
print(sum_of_five_nums(*lst))


def packing_person_info(**kwargs):
    # check the type of kwargs and it is a dict type
    # print(type(kwargs))
    # Printing dictionary items
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="Asabeneh",
      country="Finland", city="Helsinki", age=250))


for index, item in enumerate([20, 30, 40]):
    print(index, item)

countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
for index, i in enumerate(countries):
    if i == 'Finland':
        print(f'The country {i} has been found at index {index}')



# Exercises: Day 17
print('\n# 1')
names = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland', 'Estonia', 'Russia']
*nordic_countries, es, ru = names
print(nordic_countries)
print(es)
print(ru)