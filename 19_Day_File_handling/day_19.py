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
def count_number_of_lines_and_words(filepath):
    with open(filepath, encoding='UTF8') as f:
        txt = f.read()
        line_count = len(txt.splitlines())
        word_count = len(txt.split())
        return line_count, word_count

lines, words = count_number_of_lines_and_words('../data/obama_speech.txt')
# lines, words = count_number_of_lines_and_words('../data/michelle_obama_speech.txt')
# lines, words = count_number_of_lines_and_words('../data/donald_speech.txt')
# lines, words = count_number_of_lines_and_words('../data/melina_trump_speech.txt')
print('number of lines: ', lines)
print('number of words: ', words)


print('\n# 2')
import json
def most_spoken_languages(filename, num):
    with open(filename, encoding='UTF8') as f:
        countries = json.load(f)  # load 用于解析 JSON 文件，loads 用于解析 JSON 格式的字符串
    country_language = {}
    for country in countries:
        for language in country['languages']:
            if language in country_language:
                country_language[language] += 1
            else:
                country_language[language] = 1
    country_language_list = []
    for language, count in country_language.items():
        country_language_list.append((count, language))
    country_language_list.sort(reverse=True)
    return(country_language_list[:num])

file = '../data/countries_data.json'
print(most_spoken_languages(file, 10))


print('\n# 3')
import json
def most_populated_countries(filename, num):
    with open(filename, encoding='UTF8') as f:
        countries = json.load(f)
    population_list = []
    for country in countries:
        population_list.append({'country': country['name'], 'population': country['population']})
    population_list.sort(key=lambda i:i['population'], reverse=True)
    return population_list[:num]

print(most_populated_countries('../data/countries_data.json', 10))


# Exercises: Level 2
print('\nExercises: Level 2')
print('\n# 1')
# 方法一：正则表达式
import re
with open('../data/email_exchanges_big.txt') as f:
    txt = f.read()
    incoming_email_addresses = re.findall(r'From:\s+(\S+@\S+)$', txt, re.MULTILINE)
    # 上一行表示必须以From开头，后面有一个或多个空白字符，()提取邮箱地址，re.MULTILINE 使得^可以匹配每一行开头，而不只是整个文本的开头
    # print(incoming_email_addresses)

# 方法二：逐行提取
incoming_email_addresses = []
with open('../data/email_exchanges_big.txt') as f:
    for line in f:
        if line.startswith('From:'):
            email_address = line.split(':', 1)[1].strip()  # split(':', 1) 当中的1表示最多分割一次。strip() 去掉首尾空格
            incoming_email_addresses.append(email_address)
# print(incoming_email_addresses)


print('\n# 2')
def find_most_frequent_words(filename, num):
    with open(filename, encoding='UTF8') as f:
        txt = f.read()
    words = txt.split()
    words_count = {}
    for word in words:
        if word in words_count:
            words_count[word] += 1
        else:
            words_count[word] = 1
    words_count_list = []
    for word, count in words_count.items():
        words_count_list.append((count, word))
    words_count_list.sort(reverse=True)
    return(words_count_list[:num])


print('\n# 3')
# print(find_most_frequent_words('../data/obama_speech.txt', 10))
# print(find_most_frequent_words('../data/michelle_obama_speech.txt', 10))
# print(find_most_frequent_words('../data/donald_speech.txt', 10))
print(find_most_frequent_words('../data/melina_trump_speech.txt', 10))


print('\n# 4')
stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up',
              'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

import re

def clean_text(filename):
    with open(filename, encoding='UTF8') as f:
        # txt = f.read().split()  # 需要更多操作
        txt = f.read()
        txt = txt.lower()  # 全部转换为小写
        txt = re.sub(r'[^a-z\s]', '', txt)  # 只保留字母和空白字符
        txt = txt.split()
    return txt

def remove_support_words(text):
    words = []
    for word in text:
        if word not in stop_words:
            words.append(word)
    return words

# def check_text_similarity(t1, t2):
#     count_total = len(t1) + len(t2)
#     count_same = 0
#     for word in t1:
#         if word in t2:
#             count_same += 1
#     count_total_different = count_total - count_same
#     similarity = count_same / count_total_different
#     return similarity

# 用下面这种写法，避免出错
def check_text_similarity(t1, t2):
    set1 = set(t1)  # 转换为集合去除重复单词
    set2 = set(t2)
    same_words = set1.intersection(set2)  # 两篇文章共同出现的单词
    total_words = set1.union(set2)  # 两篇文章中所有不同的单词
    if len(total_words) == 0:
        return 0  # 防止两篇文章都为空时出现除以0
    similarity = len(same_words) / len(total_words)
    return similarity

Michelle = remove_support_words(clean_text('../data/michelle_obama_speech.txt'))
Melina = remove_support_words(clean_text('../data/melina_trump_speech.txt'))
print(check_text_similarity(Michelle, Melina))



print('\n# 5')
import re
def find_most_repeated_words(filename, num):
    with open(filename, encoding='UTF8') as f:
        txt = f.read()
    txt = txt.lower()
    txt = re.sub(r'[^a-z\s]', '', txt)
    words = txt.split()

    words_count = {}
    for word in words:
        if word not in stop_words:
            if word in words_count:
                words_count[word] += 1
            else:
                words_count[word] = 1
    words_count_list = []
    for word, count in words_count.items():
        words_count_list.append((count, word))
    words_count_list.sort(reverse=True)
    return(words_count_list[:num])

print(find_most_repeated_words('../data/romeo_and_juliet.txt', 10))
print(find_most_frequent_words('../data/romeo_and_juliet.txt', 10))


print('\n# 6')
import csv
# skills = ['python', 'Python']  # 不需要
with open('../data/hacker_news.csv', encoding='UTF8') as f:
    csv_reader = csv.reader(f, delimiter=',')
    # count = {}  # 错误
    count_line = 0
    for row in csv_reader:
        # for word in row:  # 错误
        #     if word in skills:
        #         count[row] += 1
        for cell in row:
            if 'python' in cell or 'Python' in cell:
                count_line += 1
                break
    # count_line = len(count)  # 错误
    print(count_line)


import csv
with open('../data/hacker_news.csv', encoding='UTF8') as f:
    csv_reader = csv.reader(f, delimiter=',')
    count_line = 0
    for row in csv_reader:
        for cell in row:
            if 'JavaScript' in cell or 'javascript' in cell or 'Javascript' in cell:
                count_line += 1
                break
    print(count_line)


import csv
with open('../data/hacker_news.csv', encoding='UTF-8') as f:
    csv_reader = csv.reader(f)
    count_line = 0
    for row in csv_reader:
        contains_java = False
        contains_javascript = False
        for cell in row:
            if 'Java' in cell:
                contains_java = True
            if 'JavaScript' in cell:
                contains_javascript = True
        if contains_java and not contains_javascript:  # 表示 contains_java 和 not contains_javascript 都要为 True
            count_line += 1
    print(count_line)

# 简便写法
import csv
with open('../data/hacker_news.csv', encoding='UTF8') as f:
    csv_reader = csv.reader(f, delimiter=',')
    count_line = 0
    for row in csv_reader:
        line = ' '.join(row)  # 简便写法
        if 'Java' in line and 'JavaScript' not in line:
            count_line += 1
    print(count_line)


# 三个一起写
import csv

python_count = 0
javascript_count = 0
java_count = 0

with open('../data/hacker_news.csv', encoding='UTF-8') as f:
    csv_reader = csv.reader(f)

    for row in csv_reader:
        line = ' '.join(row)

        if 'python' in line or 'Python' in line:
            python_count += 1

        if 'JavaScript' in line or 'javascript' in line or 'Javascript' in line:
            javascript_count += 1

        if 'Java' in line and 'JavaScript' not in line:
            java_count += 1

print('Python:', python_count)
print('JavaScript:', javascript_count)
print('Java:', java_count)