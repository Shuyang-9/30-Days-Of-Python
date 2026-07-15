f = open('../files/reading_file_example.txt')
print(f) # <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='UTF-8'>  # 我输出的结果是 encoding='cp936'

f = open('../files/reading_file_example.txt')
txt = f.read()
print(type(txt))
print(txt)
f.close()

f = open('../files/reading_file_example.txt')
lines = f.readlines()
print(type(lines))
print(lines)
f.close()


import json
# python字典
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScript", "React", "Python"]
}
# 将字典转换为JSON字符串
person_json = json.dumps(person, indent=8) # indent可以是2, 4, 8. 它漂亮地打印了。
print(type(person_json))
print(person_json)


import csv
with open('../files/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'列名为: {", ".join(row)}')
            line_count += 1
        else:
            print(f'{row[0]}来自{row[1]}的{row[2]}。 他了解{row[3]}')
            line_count += 1
    print(f'已处理{line_count}行。')


# 我们还可以使用相同的方法将数据写入csv文件
import csv
with open('../files/csv_example.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # 写入列名
    writer.writerow(['name', 'country', 'city', 'skills'])
    # 写入数据
    writer.writerow(['Asabeneh', 'Finland', 'Helsinki', 'JavaScript'])


# 要读取Excel文件，我们需要安装xlrd包。我们将使用它来读取Excel文件。
# import xlrd
# excel_book = xlrd.open_workbook('sample.xls')
# print(excel_book.nsheets)
# print(excel_book.sheet_names)




# Exercises: Day 19
# Exercises: Level 1
print('\nExercises: Level 1')
print('\n# 1')
# 方法一：正则表达式
import re
with open('../data/email_exchanges_big.txt') as f:
    txt = f.read()
    incoming_email_addresses = re.findall(r'From:\s+(\S+@\S+)$', txt, re.MULTILINE)
    # 上一行表示必须以From开头，后面有一个或多个空白字符，()提取邮箱地址，re.MULTILINE 使得^可以匹配每一行开头，而不只是整个文本的开头
    print(incoming_email_addresses)

# 方法二：逐行提取
incoming_email_addresses = []
with open('../data/email_exchanges_big.txt') as f:
    for line in f:
        if line.startswith('From:'):
            email_address = line.split(':', 1)[1].strip()  # split(':', 1) 当中的1表示最多分割一次。strip() 去掉首尾空格
            incoming_email_addresses.append(email_address)
print(incoming_email_addresses)


print('\n# 2')






print('\n# 3')




# Exercises: Level 2
print('\nExercises: Level 2')
print('\n# 1')





print('\n# 2')






print('\n# 3')





print('\n# 4')





print('\n# 5')






print('\n# 6')




