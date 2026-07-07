fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
print(fruits)

fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop()
print(removed_item)

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits)  # set()

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st2.difference(st1)) # set() : st2 - st1
print(st1.difference(st2)) # {'item1', 'item4'} => st1\st2  : st2 - st1

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
print(python.difference(dragon))     # {'p', 'y', 't', 'h'} 无序排列
print(dragon.difference(python))     # {'d', 'r', 'a', 'g'} 无序排列

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3', 'item5'}
# 意思是 (A\B)∪(B\A)
print(st2.symmetric_difference(st1))  # {'item1', 'item4', 'item5'}
print(st1.symmetric_difference(st2))  # 同上
print(st2 ^ st1)  # 或者用 ^ 符号表示

# 语法
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st2.isdisjoint(st1))  # 错误

# Exercises: Day 7
# Exercises: Level 1
print('\nExercises: Level 1')
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

print('\n# 1')
print(len(it_companies))

print('\n# 2')
it_companies.add('Twitter')
print(it_companies)

print('\n# 3')
it_companies.update({'Meta', 'Sina'})
print(it_companies)

print('\n# 4')
it_companies.remove('Sina')
print(it_companies)

print('\n# 5')
# 可以使用 remove() 方法从集合中移除一个元素。如果找不到该元素，remove() 方法会抛出错误，因此最好先检查该元素是否存在于集合中。
# discard() 方法则不会抛出任何错误。


# Exercises: Level 2
print('\nExercises: Level 2')
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

print('\n# 1')
print(A.union(B))

print('\n# 2')
print(A.intersection(B))

print('\n# 3')
print(A.issubset(B))

print('\n# 4')
print(A.isdisjoint(B))

print('\n# 5')
print(A.union(B))
print(B.union(A))

print('\n# 6')
print(A.symmetric_difference(B))

print('\n# 7')
del A
del B


# Exercises: Level 3
print('\nExercises: Level 3')
age = [22, 19, 24, 25, 26, 24, 25, 24]
print('\n# 1')
age_set = set(age)
print(len(age) > len(age_set))
print(len(age))
print(len(age_set))

print('\n# 2')
# string: 字符串，用来存储文本，例如 'hello'
# list: 列表，有序、可修改、允许重复值，例如 [1, 2, 2, 3]
# tuple: 元组，有序、不可修改、允许重复值，例如 (1, 2, 2, 3)
# set: 集合，无序、可修改、不允许重复值，例如 {1, 2, 3}

print('\n# 3')
sentence = "I am a teacher and I love to inspire and teach people"
sentence_list = sentence.split(' ')
sentence_set = set(sentence_list)
print(len(sentence_set))