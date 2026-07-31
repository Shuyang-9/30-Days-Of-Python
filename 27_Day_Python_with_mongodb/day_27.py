from flask import Flask, render_template
from pymongo import MongoClient
import os

# MongoDB连接
MONGODB_URI = "mongodb+srv://shuyang:30daysofpython@30daysofpython.ymd6jyv.mongodb.net/?appName=30DaysofPython"
client = MongoClient(MONGODB_URI)
print(client.list_database_names())

# 数据库
db = client["thirty_days_of_python"]

# 创建students集合并插入数据
# db.students.insert_one({
#     "name": "Asabeneh",
#     "country": "Finland",
#     "city": "Helsinki",
#     "age": 250
# })
# 多条信息
# students = [
#         {'name':'David','country':'UK','city':'London','age':34},
#         {'name':'John','country':'Sweden','city':'Stockholm','age':28},
#         {'name':'Sami','country':'Finland','city':'Helsinki','age':25},
#     ]
# for student in students:
#     db.students.insert_one(student)

# print(client.list_database_names())

# # Flask
# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "MongoDB Flask connection successful!"

# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 5000))
#     app.run(debug=True, host="0.0.0.0", port=port)


# 查找
student = db.students.find_one()  # 返回第一个条目
# student = db.students.find_one({'_id':ObjectId('5df68a23f106fe2d315bbc8c')})  # 返回特定的对象
print(student)

# 查找所有
# students = db.students.find()
# for student in students:
#     print(student)

# 限制文档数量
# db.students.find().limit(3)

# 可以通过在_find({}, {})_中传递第二个对象来指定要返回的字段。0表示不包含，1表示包含，但我们不能混合使用0和1，除了_id。
# students = db.students.find({}, {"_id":0,  "name": 1, "country":1})  # 0表示不包含，1表示包含
# for student in students:
#     print(student)


# 通过一个查询对象过滤文档
# query = {"country":"Finland"}
# query = {"country":"Finland", "city":"Helsinki"}
# students = db.students.find(query)
# for student in students:
#     print(student)

# 带有修饰符的查询
# query = {"age":{"$gt":30}}  # greater than
# students = db.students.find(query)
# for student in students:
#     print(student)

# 排序
# students = db.students.find().sort('name')  # 默认情况下排序是升序
# students = db.students.find().sort('name',-1)  # 添加-1参数将排序更改为降序
# for student in students:
#     print(student)

# 使用查询进行更新
# query = {'age':250}
# new_value = {'$set':{'age':38}}
# db.students.update_one(query, new_value)
# # 让我们检查结果，看看年龄是否被修改
# for student in db.students.find():
#     print(student)

# 删除一个查询对象参数。只删除第一次出现的。
# query = {'name':'John'}
# db.students.delete_one(query)
# # 让我们检查结果，看看年龄是否被修改
# for student in db.students.find():
#     print(student)

# 删除一个collection
# db.students.drop()


app = Flask(__name__)
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)