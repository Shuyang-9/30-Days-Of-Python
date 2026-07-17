# import requests
# from bs4 import BeautifulSoup

# url = 'https://archive.ics.uci.edu/dataset/10/automobile'

# # 使用requests的get方法从url获取数据
# response = requests.get(url)
# # 检查状态
# status = response.status_code
# print(status) # 200表示获取成功

# import requests
# from bs4 import BeautifulSoup
# url = 'https://archive.ics.uci.edu/dataset/10/automobile'

# response = requests.get(url)
# content = response.content # 从网站获取所有内容
# soup = BeautifulSoup(content, 'html.parser') # beautiful soup将给我们一个解析的机会
# print(soup.title) # <title>UCI Machine Learning Repository: Data Sets</title>
# print(soup.title.get_text()) # UCI Machine Learning Repository: Data Sets
# print(soup.body) # 给出网站上的整个页面
# print(response.status_code)

# tables = soup.find_all('table', {'cellpadding':'3'})
# # 我们定位cellpadding属性值为3的表格
# # 我们可以使用id、class或HTML标签进行选择，有关更多信息，请查看beautifulsoup文档
# table = tables[0] # 结果是一个列表，我们从中提取数据
# for td in table.find('tr').find_all('td'):
#     print(td.text)



# Exercises: Day 22
print('\n# 1')
# import requests
# from bs4 import BeautifulSoup
# import json

# url = 'http://www.bu.edu/president/boston-university-facts-stats/'
# response = requests.get(url)
# print(response.status_code)
# content = response.content
# soup = BeautifulSoup(content, 'html.parser')
# print(soup.title)
# print(soup.title.get_text())

# for tag in soup.find_all(['h1', 'h2', 'h3', 'h4']):
#     print(tag.name, tag.get_text(strip=True))
# # for li in soup.find_all('li'):
# #     print(li.get_text(strip=True))

# groups = soup.find_all('h4', class_='stat-group-title')
# for group in groups:
#     print(group.get_text(strip=True))

# titles = soup.find_all('h3', class_='bu-stat-title')
# values = soup.find_all('span', class_='bu-stat-value-field')

# for title, value in zip(titles, values):
#     print(title.get_text(strip=True), value.get_text(strip=True))

# labels = soup.find_all('span', class_='stat-label')
# figures = soup.find_all('span', class_='stat-figure')

# for label, figure in zip(labels, figures):
#     print(label.get_text(strip=True), figure.get_text(strip=True))

# card_titles = soup.find_all('h3', class_='bu-stat-title')

# for title in card_titles:
#     parent = title.find_parent()
#     value_parts = parent.find_all('span', class_='bu-stat-value-field')
#     name = title.get_text(strip=True)
#     value = ''.join(part.get_text(strip=True) for part in value_parts)
#     print(name, ':', value)
import requests
from bs4 import BeautifulSoup
import json
url = 'https://www.bu.edu/president/boston-university-facts-stats/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
data = {}
group_titles = soup.find_all('h4', class_='stat-group-title')

for group in group_titles:
    group_name = group.get_text(strip=True)
    data[group_name] = {}
    for tag in group.find_all_next():
        if tag.name == 'h4' and 'stat-group-title' in tag.get('class', []) and tag != group:
            break  # 如果遇到下一个 h4.stat-group-title，说明当前 group 结束
        # 第一种结构：h3.bu-stat-title + span.bu-stat-value-field
        if tag.name == 'h3' and 'bu-stat-title' in tag.get('class', []):
            title = tag.get_text(strip=True)
            value_parts = []
            # 从这个 h3 后面继续找，直到遇到下一个 h3 或 h4
            for next_tag in tag.find_all_next():
                if next_tag.name == 'h3' and 'bu-stat-title' in next_tag.get('class', []):
                    break
                if next_tag.name == 'h4' and 'stat-group-title' in next_tag.get('class', []):
                    break
                if next_tag.name == 'span' and 'bu-stat-value-field' in next_tag.get('class', []):
                    value_parts.append(next_tag.get_text(strip=True))
            value = ''.join(value_parts)
            data[group_name][title] = value
        # 第二种结构：span.stat-label + span.stat-figure
        if tag.name == 'span' and 'stat-label' in tag.get('class', []):
            label = tag.get_text(strip=True)
            parent = tag.find_parent()
            figure_tag = parent.find('span', class_='stat-figure')
            if figure_tag:
                figure = figure_tag.get_text(strip=True)
                data[group_name][label] = figure
print(data)
with open('bu_facts_stats.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)


print('\n# 2')









print('\n# 3')








