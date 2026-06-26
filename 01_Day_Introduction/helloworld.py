# Introduction
# Day 1 - 30DaysOfPython Challenge

print("Hello World!")   # print hello world

print(2 + 3)   # addition(+)
print(3 - 1)   # subtraction(-)
print(2 * 3)   # multiplication(*)
print(3 + 2)   # addition(+)
print(3 - 2)   # subtraction(-)
print(3 * 2)   # multiplication(*)
print(3 / 2)   # division(/)
print(3 ** 2)  # exponential(**)
print(3 % 2)   # modulus(%) 取余
print(3 // 2)  # Floor division operator(//) 整除

# 尝试
print(2 / 3)  # division(/)
print(8 % 3)   # modulus(%) 取余

# Checking data types

print(type(10))                  # Int
print(type(3.14))                # Float
print(type(1 + 3j))              # Complex，1为实部，3j为虚部，在 Python（以及电气工程领域）中，用j代替数学中的i
print(type('Asabeneh'))          # String
print(type([1, 2, 3]))           # List
print(type({'name': 'Asabeneh'}))  # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, "apple")))  # Tuple

# 尝试
latitude, longitude = (39.9, 116.4)
print(latitude)   # 39.9
print(longitude)  # 116.4

person = {
    "name": "Tom",
    "age": 25,
    "city": "Shanghai",
    "courses": ["Python", "Data Science", "Machine Learning"]
}
print(person["name"])  # Tom
person["age"] = 26  # 修改年龄
print(person["age"])  # 26
person["country"] = "China"  # 添加国家
print(person)

names = ["Tom", "Tom", "Jack", "Mary"]
unique_names = set(names)
print(unique_names)  # 去重

# Find an Euclidean distance between (2, 3) and (10, 8)
print(((10 - 2) ** 2 + (8 - 3) ** 2) ** 0.5)

# 方法2
x1, y1 = 2, 3
x2, y2 = 10, 8
distance = ((x2-x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(distance)