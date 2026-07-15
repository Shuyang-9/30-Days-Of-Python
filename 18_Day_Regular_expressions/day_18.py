# match
import re

txt = 'I love to teach python and javaScript'
# 它返回一个带有span和match的对象
match = re.match('I love to teach', txt, re.I)
print(match)  # <re.Match object; span=(0, 15), match='I love to teach'>
# 我们可以使用span获取匹配的起始和结束位置，作为元组
span = match.span()
print(span)     # (0, 15)
# 让我们从span中找到起始和结束位置
start, end = span
print(start, end)  # 0, 15
substring = txt[start:end]
print(substring)       # I love to teach

txt = 'I love to teach python and javaScript'
match = re.match('I like to teach', txt, re.I)
print(match)  # None


# search
import re

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It returns an object with span and match
match = re.search('first', txt, re.I)
print(match)  # <re.Match object; span=(100, 105), match='first'>
# We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span)     # (100, 105)
# Lets find the start and stop position from the span
start, end = span
print(start, end)  # 100 105
substring = txt[start:end]
print(substring)       # first


# findall
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It return a list
matches = re.findall('language', txt, re.I)
print(matches)  # ['language', 'language']

matches1 = re.findall('Python|python', txt)
print(matches1)

matches2 = re.findall('[Pp]ython', txt)
print(matches2)


# replace a substring: sub
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.I recommend JavaScript for a first programming language
# OR
match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.I recommend JavaScript for a first programming language


txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing.
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs.
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches = re.sub('%', '', txt)
print(matches)


# writing RegEx patterns
import re

regex_pattern = r'apple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches)  # ['apple']

# To make case insensitive adding flag '
matches = re.findall(regex_pattern, txt, re.I)
print(matches)  # ['Apple', 'apple']
# or we can use a set of characters method
regex_pattern = r'[Aa]pple'  # this mean the first letter could be Apple or apple
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']


# []
regex_pattern = r'[Aa]pple|[Bb]anana' # 这意味着Apple或apple或Banana或banana
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'banana', 'apple', 'banana']

regex_pattern = r'[a].'  # this square bracket means a and . means any character except new line
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['an', 'an', 'an', 'a ', 'ar']

regex_pattern = r'[a].+'  # . any character, + any character one or more times
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']

regex_pattern = r'[a].*'  # . any character, * any character zero or more times
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']

txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail'  # ? 表示零次或一次
matches = re.findall(regex_pattern, txt)
print(matches)  # ['e-mail', 'email', 'Email', 'E-mail']






# Exercises: Day 18
# Exercises: Level 1
print('\nExercises: Level 1')
print('\n# 1')
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
words = re.findall(r'\w+', paragraph)
print(words)
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
word_count_list = list(word_count.items())
word_count_list.sort(key=lambda item:item[1], reverse=True)
print(word_count_list)


print('\n# 2')
points = ['-12', '-4', '-3', '-1', '0', '4', '8']
sorted_points = []
for i in points:
    if int(i) not in sorted_points:
        sorted_points.append(int(i))
sorted_points.sort()
print(sorted_points)
distance = sorted_points[-1] - sorted_points[0]
print(distance)


# Exercises: Level 2
print('\nExercises: Level 2')
print('\n# 1')
import re

def is_valid_variable(item):
    # if item == r'^[A-Za-z]\w+':  # 写法错误，正确写法见下一行
    # if re.fullmatch(r'[A-Za-z_]\w*', item):  # 判断整个字符串用 fullmatch
    if re.match(r'^[A-Za-z_]\w*$', item):  # 或者用这种写法，match 并且把 ^ $ 都写上
        return True
    else:
        return False
print(is_valid_variable('first_name'))
print(is_valid_variable('first-name'))
print(is_valid_variable('1first_name'))
print(is_valid_variable('firstname'))


print('\n# 2')
text = '''
HTML
Hypertext Markup Language (HTML) is the standard markup language for documents designed to be displayed in a web browser. It can be assisted by technologies such as Cascading Style Sheets (CSS) and scripting languages such as JavaScript.

Web browsers receive HTML documents from a web server or from local storage and render the documents into multimedia web pages. HTML describes the structure of a web page semantically and originally included cues for the appearance of the document.

HTML elements are the building blocks of HTML pages. With HTML constructs, images and other objects such as interactive forms may be embedded into the rendered page. HTML provides a means to create structured documents by denoting structural semantics for text such as headings, paragraphs, lists, links, quotes and other items. HTML elements are delineated by tags, written using angle brackets. Tags such as <img /> and <input /> directly introduce content into the page. Other tags such as <p> surround and provide information about document text and may include other tags as sub-elements. Browsers do not display the HTML tags, but use them to interpret the content of the page.

HTML can embed programs written in a scripting language such as JavaScript, which affects the behavior and content of web pages. Inclusion of CSS defines the look and layout of content. The World Wide Web Consortium (W3C), former maintainer of the HTML and current maintainer of the CSS standards, has encouraged the use of CSS over explicit presentational HTML since 1997.
'''
import re
# clean_text = re.sub(r'^<\w*\W*>$', '', text)  # 错误
clean_text = re.sub(r'<[^>]+>', '', text)  # [^>]+ 表示一个或多个不是 > 的字符
print(clean_text)



# Exercises: Level 3
print('\nExercises: Level 3')
print('\n# 1')
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

import re

def clean_text(item):
    clean_item = re.sub(r'[^\w\s]*', '', item)
    return clean_item

print(clean_text(sentence))

cleaned_text = re.findall(r'\w+', clean_text(sentence))

def most_frequent_words(text):
    word_count = {}
    for i in text:
        if i in word_count:
            word_count[i] += 1
        else:
            word_count[i] = 1
    word_count_list = []
    for word, count in word_count.items():
        word_count_list.append((count, word))  # 注意前后顺序
    word_count_list.sort(reverse=True)  # 直接按照倒序排列，否则字母的顺序也会重新排列，本题中需要按照它原来出现的位置选前三个
    return word_count_list[:3]
print(most_frequent_words(cleaned_text)) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]


print('\n# 2')
email_address = '''
asabeneh@gmail.com
alex@yahoo.com
kofi@yahoo.com
doe@arc.gov
asabeneh.com
asabeneh@gmail
alex@yahoo
'''

def extract_email_address(items):
    clean_email_address = re.findall(r'\S+@[A-Za-z0-9]+\.[A-Za-z]+', items)
    return clean_email_address

print(extract_email_address(email_address))