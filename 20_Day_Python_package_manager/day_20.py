import webbrowser # web浏览器模块用于打开网站

# 网址列表：Python
url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://github.com/Asabeneh',
    'https://twitter.com/Asabeneh',
]

# 在不同的标签页中打开上面的网站列表
# for url in url_lists:
#     webbrowser.open_new_tab(url)


# import requests # importing the request module

# url = 'https://www.w3.org/robots.txt'  # text from a website

# response = requests.get(url) # opening a network and fetching a data
# print(response)
# print(response.status_code) # status code, success:200
# print(response.headers)     # headers information
# print(response.text) # gives all the text from the page


# import requests
# url = 'https://restcountries.eu/rest/v5/all'  # countries api
# response = requests.get(url)  # opening a network and fetching a data
# print(response) # response object
# print(response.status_code)  # status code, success:200
# countries = response.json()
# print(countries[:1])  # we sliced only the first country, remove the slicing to see all countries





# Exercises: Day 20
# print('\n# 1')
# import requests
# import re
# url = 'https://www.gutenberg.org/cache/epub/1513/pg1513.txt'
# response = requests.get(url)
# txt = response.text
# txt = txt.lower()
# txt = re.sub('[^A-Za-z]+', ' ', txt)
# words = txt.split()
# word_count = {}
# for word in words:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1
# word_count_list = list(word_count.items())
# print(word_count_list[:10])


print('\n# 2')
import requests
from statistics import *

url = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(url)
cats_list = response.json()
print(type(cats_list))

weight_list = []
for cat in cats_list:
    weight = cat['weight']['metric']
    w1 = int(weight.split('-')[0].strip())
    w2 = int(weight.split('-')[1].strip())
    w = (w1 + w2) / 2
    weight_list.append(w)
print(min(weight_list))
print(max(weight_list))
print(mean(weight_list))
print(median(weight_list))
print(stdev(weight_list))

lifespan_list = []
for cat in cats_list:
    lifespan = cat['life_span']
    l1 = int(lifespan.split('-')[0].strip())
    l2 = int(lifespan.split('-')[1].strip())
    l = (l1 + l2) / 2
    lifespan_list.append(l)
print(min(lifespan_list))
print(max(lifespan_list))
print(mean(lifespan_list))
print(median(lifespan_list))
print(stdev(lifespan_list))

country_list = {}
for cat in cats_list:
    if cat['origin'] in country_list:
        country_list[cat['origin']] += 1
    else:
        country_list[cat['origin']] = 1
print(country_list)


print('\n# 3')

print('\n# 4')
