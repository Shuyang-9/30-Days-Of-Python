# Exercises: Day 6
# Exercises: Level 1
print('Exercises: Level 1')
print('\n# 1')
empty_tuple = tuple()
print(empty_tuple)

print('\n# 2')
sisters = ('Subah', 'Grace')
brothers = ('Nate', 'Ali')
print(sisters)
print(brothers)

print('\n# 3')
siblings = brothers + sisters
print(siblings)

print('\n# 4')
print(len(siblings))

print('\n# 5')
# family_members = list(siblings)
# print(family_members)
# family_members.append('J')
# family_members.append('QH')
# 题目要求modify tuple
family_members = siblings + ('J', 'QH')
print(family_members)


# Exercises: Level 2
print('\nExercises: Level 2')
print('\n# 1')
siblings, parents = family_members[:4], family_members[-2:]
print(siblings)
print(parents)

print('\n# 2')
fruits = ('apple', 'pear', 'peach')
vegetables = ('tomato', 'cucumber')
animal_products = ('milk', 'egg', 'cheese', 'honey')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

print('\n# 3')
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

print('\n# 4')
food_stuff_lt_new = food_stuff_lt[:4] + food_stuff_lt[5:]
print(food_stuff_lt_new)

print('\n# 5')
del food_stuff_lt[:3]
del food_stuff_lt[-3:]
print(food_stuff_lt)

print('\n# 6')
del food_stuff_tp
# print(food_stuff_tp)

print('\n# 7')
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)