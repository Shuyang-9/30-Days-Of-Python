# 字典长度
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(len(dct))  # 4

# 访问字典项
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct['key1'])  # value1
print(dct['key4'])  # value4

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
print(person['first_name']) # Asabeneh
print(person['country'])    # Finland
print(person['skills'])     # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person['skills'][0])  # JavaScript
print(person['address']['street']) # Space street
# print(person['city'])       # Error

print(person.get('first_name')) # Asabeneh
print(person.get('country'))    # Finland
print(person.get('skills')) #['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person.get('city'))   # None

person['job_title'] = 'Instructor'
person['skills'].append('HTML')
print(person)

person.pop('first_name')
person.popitem()
del person['country']
print(person)

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])



# Exercises: Day 8
print('\n# 1')
dog = {}
print('\n# 2')
dog['name'] = 'Bob'
dog['color'] = 'Yellow'
dog['breed'] = 'Missing'
dog['legs'] = 4
dog['age'] = 2
print(dog)

print('\n# 3')
student = {'first_name':'Shuyang', 'last_name':'Shi', 'gender':'female', 'age':25, 'marital status':'no', 'skills':['read', 'write', 'draw'], 'country':'China', 'city':'CZcity', 'address':'Sipailou#2'}
print(student)

print('\n# 4')
print(len(student))

print('\n# 5')
print(student['skills'])
print(type(student['skills']))

print('\n# 6')
student['skills'].append('run')
print(student)

print('\n# 7')
print(list(student.keys()))  # 题目中要求 as a list 所以需要在外面套一层 list()

print('\n# 8')
print(list(student.values()))

print('\n# 9')
print(list(student.items()))

print('\n# 10')
student.pop('first_name')
print(student)

print('\n# 11')
del student


