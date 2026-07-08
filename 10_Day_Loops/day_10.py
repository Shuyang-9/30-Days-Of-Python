# while loops
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)

# for loops
language = 'Python'
for letter in language:
    print(letter)

for i in range(len(language)):
    print(language[i])

numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key) #仅输出键
print(person.items())
for key, value in person.items():
    print(key, value) # 这样我们可以在迭代的过程中同时访问键和值

print("\n")
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # 简而言之，对于简短的条件，需要同时使用if和else语句
print('outside the loop')

# range function
print("\n")
lst = list(range(11))
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 2 arguments indicate start and end of the sequence, step set to default 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}

# for backward from start to end
lst = list(range(11,0,-2))
print(lst) # [11,9,7,5,3,1]

# nested for loop
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)

# for else
for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)



# Exercises: Day 10
# Exercises: Level 1
print('\nExercises: Level 1')
print('\n# 1')
for i in range(0, 11):
    print(i)

i = 0
while 0 <= i <= 10:
    print(i)
    i += 1

print('\n# 2')
for i in range(10, -1, -1):
    print(i)

i = 10
while 0 <= i <= 10:
    print(i)
    i -= 1

print('\n# 3')
i = "#######"
count = 1
while 0 < count < 8:
    print(i[:count])
    count += 1

# 或者写成
for i in range(1, 8):
    print("#" * i)

print('\n# 4')
# 错误。会单独打印每一个#，不会打印成一排。
# i = "# # # # # # # #"
# for count in range(1, 9):
#     for i in "# # # # # # # #":
#         print(i)
for row in range(8):
    for col in range(8):
        print("#", end=" ")
    print()

print('\n# 5')
x = 0
for x in range(0, 11):
    print(f"{x} * {x} = {x*x}")

print('\n# 6')
lst = ['Python', 'Numpy','Pandas','Django', 'Flask']
for i in range(len(lst)):
    print(lst[i])

for skill in lst:
    print(skill)

print('\n# 7')
for i in range(0, 101):
    if i % 2 == 0:
        print(i)

print('\n# 8')
for i in range(0, 101):
    if i % 2 == 1:
        print(i)


print('\nExercises: Level 2')
print('\n# 1')
total = 0
for i in range(0, 101):
    total += i
print(f"The sum of all numbers is {total}.")

print('\n# 2')
sum_even = 0
sum_odd = 0
for i in range(0, 101):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i
print(f"The sum of all evens is {sum_even}. And the sum of all odds is {sum_odd}.")


print('\nExercises: Level 3')
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "data"))

from countries import countries
from countries_data import countries_data

print('\n# 1')
for country in countries:
    if "land" in country:  # 或者用 country.lower() 表示不区分大小写
        print(country)

print('\n# 2')
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_new = []
number = len(fruits)
for i in range(number-1, -1, -1):
    fruits_new.append(fruits[i])
print(fruits_new)

print('\n# 3')
print('#3.1')
languages = []

for country in countries_data:
    for language in country["languages"]:
        if language not in languages:
            languages.append(language)

print("Total number of languages: ", len(languages))


print('\n#3.2')
language_count = {}

for country in countries_data:
    for language in country["languages"]:
        if language in language_count:
            language_count[language] += 1
        else:
            language_count[language] = 1

# print(language_count)  # 仅查看，无作用

language_count_list = list(language_count.items())

# print(language_count_list)  # 仅查看，无作用

language_count_list.sort(key=lambda item: item[1], reverse=True)

print("Ten most spoken languages:")
for language, count in language_count_list[:10]:
    print(language, count)

print('\n#3.3')
population_list = []

for country in countries_data:
    population_list.append((country["name"], country["population"]))

# print(population_list)  # 仅查看，无作用

population_list.sort(key=lambda item: item[1], reverse=True)

print("Ten most populated countries:")
for country, population in population_list[:10]:
    print(country, population)