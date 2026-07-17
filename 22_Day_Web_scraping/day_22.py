# import requests
# from bs4 import BeautifulSoup

# url = 'https://archive.ics.uci.edu/dataset/10/automobile'

# # 使用requests的get方法从url获取数据
# response = requests.get(url)
# # 检查状态
# status = response.status_code
# print(status) # 200表示获取成功

import requests
from bs4 import BeautifulSoup
url = 'https://archive.ics.uci.edu/dataset/10/automobile'

response = requests.get(url)
content = response.content # 从网站获取所有内容
soup = BeautifulSoup(content, 'html.parser') # beautiful soup将给我们一个解析的机会
print(soup.title) # <title>UCI Machine Learning Repository: Data Sets</title>
print(soup.title.get_text()) # UCI Machine Learning Repository: Data Sets
print(soup.body) # 给出网站上的整个页面
print(response.status_code)

tables = soup.find_all('table', {'cellpadding':'3'})
# 我们定位cellpadding属性值为3的表格
# 我们可以使用id、class或HTML标签进行选择，有关更多信息，请查看beautifulsoup文档
table = tables[0] # 结果是一个列表，我们从中提取数据
for td in table.find('tr').find_all('td'):
    print(td.text)



# Exercises: Day 22
print('\n# 1')
# import requests
# from bs4 import BeautifulSoup
# import json

# url = 'http://www.bu.edu/president/boston-university-facts-stats/'
# response = requests.get(url)
# if response.status_code == 200:
#     soup = BeautifulSoup(content, 'html.parser')
#     data = {}
#     items = soup.find_all('h4')
#     for item in items:
#         key = item.get_text(strip=True)
#         value = item.find_text('p').get_text(strip=True)
#         data[key] = value
#     with open('bu_facts.json', 'w', encoding='utf-8') as f:
#         json.dump(data, f, indent=4, ensure_ascii=False)
#     print('JSON file created successfully.')
# else:
#     print('Failed: ', response.status_code)







print('\n# 2')









print('\n# 3')








