# Exercises: Day 12
# Exercises: Level 1
print('\nExercises: Level 1')
print('\n# 1')
import random
import string

def random_use_id():
    characters = string.ascii_letters + string.digits
    user_id = ''
    for i in range(6):
        user_id += random.choice(characters)  # choice 是 random 模块中的一个函数。作用是从一个序列中随机选出一个元素。
    return user_id
print(random_use_id())


print('\n# 2')
import random
import string

def user_id_gen_by_user():
    character_number = int(input('Enter the number of characters: '))  # 注意题目要求输入值
    id_number = int(input('Enter the number of IDs: '))

    characters = string.ascii_letters + string.digits
    for i in range(id_number):
        user_id = ''
        for m in range(character_number):
            user_id += random.choice(characters)
        print(user_id)
user_id_gen_by_user()


print('\n# 3')
from random import randint

def rgb_color_gen():
    a = randint(0, 255)
    b = randint(0, 255)
    c = randint(0, 255)
    print(f'rgb({a}, {b}, {c})')  # 或者改为 return f'rgb({a}, {b}, {c})'
rgb_color_gen()  # 和上一行一起修改为 print(rgb_color_gen())


# Exercises: Level 2
print('\nExercises: Level 2')
print('\n# 1')
# import string
import random

def list_of_hexa_colors(number):
    characters = '0123456789abcdef'  # 注意可以自己定义需要的值
    colors = []
    for i in range(number):
        color = '#'
        for j in range(6):
            color += random.choice(characters)
        colors.append(color)
    return colors
print(list_of_hexa_colors(3))


print('\n# 2')
import random
def list_of_rgb_colors(number):
    colors = []
    for i in range(number):
        a = random.randint(0, 255)  # 为避免出现调用错误，将 random. 补上。或者直接写 from random import randint
        b = random.randint(0, 255)
        c = random.randint(0, 255)
        colors.append(f'rgb({a}, {b}, {c})')
    return colors
print(list_of_rgb_colors(3))


print('\n# 3')
import random
def generate_colors(color_type, number):
    colors = []
    if color_type == 'hexa':
        characters = '0123456789abcdef'
        for i in range(number):
            color = '#'
            for j in range(6):
                color += random.choice(characters)
            colors.append(color)
        return colors
    elif color_type == 'rgb':
        for i in range(number):
            a = random.randint(0, 255)
            b = random.randint(0, 255)
            c = random.randint(0, 255)
            colors.append(f'rgb({a}, {b}, {c})')
        return colors
    else:
        return 'Wrong Type'
print(generate_colors('hexa', 3))
print(generate_colors('hexa', 1))
print(generate_colors('rgb', 3))
print(generate_colors('rgb', 1))


# Exercises: Level 3
print('\nExercises: Level 3')
print('\n# 1')
import random
def shuffle_list(lst):
    random.shuffle(lst)
    return lst
print(shuffle_list([1, 1, 2, 7, 6, 8, 9]))


print('\n# 2')
import random
def seven_random_numbers():
    return random.sample(range(10), 7)
print(seven_random_numbers())