user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
    print('访问授权！')
else:
    print('访问拒绝！')



# Exercises: Day 9
# Exercises: Level 1
print('\nExercises: Level 1')
print('\n# 1')
age = int(input("Enter your age: "))  # 注意格式需要转换成 int
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    print(f"You need {18-age} more years to learn to drive.")

print('\n# 2')
my_age = 25
your_age = int(input("Enter your age: "))
if your_age > my_age:
    if your_age - my_age == 1:
        print("You are 1 year older than me.")
    else:
        print(f"You are {your_age - my_age} years older than me.")
elif your_age < my_age:
    if my_age - your_age == 1:
        print("You are 1 year younger than me.")
    else:
        print(f"You are {my_age - your_age} years younger than me.")
else:
    print("We are the same age.")


print('\n# 3')
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))
if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")


# Exercises: Level 2
print('\nExercises: Level 2')
print('\n# 1')
score = int(input("Enter your score: "))
if 90 <= score <= 100:
    print("A")
elif 80 <= score <= 89:
    print("B")
elif 70 <= score <= 79:
    print("C")
elif 60 <= score <= 69:
    print("D")
else:
    print("F")

print('\n# 2')
month = input("Enter the month: ")
if month in ['September', 'October', 'November']:
    print("the season is Autumn")
elif month in ['December', 'January', 'February']:
    print("the season is Winter")
elif month in ['March', 'April', 'May']:
    print("the season is Spring")
else:
    print("the season is Summer")

print('\n# 3')
fruit_new = input("Enter the fruit: ")
fruits = ['banana', 'orange', 'mango', 'lemon']
if fruit_new in fruits:
    print("That fruit already exists in the list")
else:
    fruits.append(fruit_new)  # 注意写法
    print(fruits)


# Exercises: Level 3
print('\nExercises: Level 3')
print('\n# 1')
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if "skills" in person:  # 注意写法
    print(person["skills"][len(person["skills"])//2])

if "skills" in person:  # 注意写法
    if "Python" in person["skills"]:
        print("The person has Python skill.")
    else:
        print("The person does not have Python skill.")

# 这一段写法错误
# if person["skills"] == ["JavaScript", "React"] or person["skills"] == ["React", "JavaScript"]:
#     print("He is a front end developer")
# elif ["Node", "Python", "MongoDB"] in person["skills"]:  # 错误，是字符串，不是列表
#     print("He is a back end developer")
# elif ["React", "Node", "MongoDB"] in person["skills"]:  # 错误，是字符串，不是列表。可和上面的判断修改顺序
#     print("He is a fullstack developer")
# else:
#     print("unknown title")

if person["skills"] == ["JavaScript", "React"] or person["skills"] == ["React", "JavaScript"]:
    print("He is a front end developer")
elif "React" in person["skills"] and "Node" in person["skills"] and "MongoDB" in person["skills"]:
    print("He is a fullstack developer")
elif "Node" in person["skills"] and "Python" in person["skills"] and "MongoDB" in person["skills"]:
    print("He is a back end developer")
else:
    print("unknown title")


if person["is_married"] == True and person["country"] == "Finland":
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")