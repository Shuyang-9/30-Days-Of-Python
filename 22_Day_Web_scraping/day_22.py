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

# # 完整
# import requests
# from bs4 import BeautifulSoup
# import json
# url = 'https://www.bu.edu/president/boston-university-facts-stats/'
# response = requests.get(url)
# soup = BeautifulSoup(response.content, 'html.parser')
# data = {}
# group_titles = soup.find_all('h4', class_='stat-group-title')

# for group in group_titles:
#     group_name = group.get_text(strip=True)
#     data[group_name] = {}
#     for tag in group.find_all_next():
#         if tag.name == 'h4' and 'stat-group-title' in tag.get('class', []) and tag != group:
#             break  # 如果遇到下一个 h4.stat-group-title，说明当前 group 结束
#         # 第一种结构：h3.bu-stat-title + span.bu-stat-value-field
#         if tag.name == 'h3' and 'bu-stat-title' in tag.get('class', []):
#             title = tag.get_text(strip=True)
#             value_parts = []
#             # 从这个 h3 后面继续找，直到遇到下一个 h3 或 h4
#             for next_tag in tag.find_all_next():
#                 if next_tag.name == 'h3' and 'bu-stat-title' in next_tag.get('class', []):
#                     break
#                 if next_tag.name == 'h4' and 'stat-group-title' in next_tag.get('class', []):
#                     break
#                 if next_tag.name == 'span' and 'bu-stat-value-field' in next_tag.get('class', []):
#                     value_parts.append(next_tag.get_text(strip=True))
#             value = ''.join(value_parts)
#             data[group_name][title] = value
#         # 第二种结构：span.stat-label + span.stat-figure
#         if tag.name == 'span' and 'stat-label' in tag.get('class', []):
#             label = tag.get_text(strip=True)
#             parent = tag.find_parent()
#             figure_tag = parent.find('span', class_='stat-figure')
#             if figure_tag:
#                 figure = figure_tag.get_text(strip=True)
#                 data[group_name][label] = figure
# print(data)
# with open('bu_facts_stats.json', 'w', encoding='utf-8') as f:
#     json.dump(data, f, ensure_ascii=False, indent=4)



print('\n# 2')
# import requests
# from bs4 import BeautifulSoup
# import json

# # 获取网页
# url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'
# headers = {"User-Agent": "Mozilla/5.0"}  # 避免出现自动爬虫请求 python-requests
# response = requests.get(url, headers=headers)
# print(response.status_code)
# content = response.content
# soup = BeautifulSoup(content, 'html.parser')
# print(soup.title)

# # 查看网页一共有几张表格，确认第几个表格是我们需要的
# tables = soup.find_all('table')
# print(len(tables))
# for i, table in enumerate(tables):
#     print(i, table.get_text(strip=True)[:100])
# # 已确认表格序号，先提取表头，同时去除上标
# table = tables[0]
# header_row = table.find("tr")
# headers = []
# for th in header_row.find_all('th'):
#     for sup in th.find_all("sup"):
#         sup.decompose()
#     headers.append(th.get_text(" ", strip=True))
# print(headers)

# columns = ['No.', 'Name (birth–death)', 'Term', 'Party', 'Election', 'Vice President']  # 列名
# span_cache = {}  # 保存跨行内容
# records = []
# rows = table.find_all("tr")[1:]
# for row in rows:
#     cells = row.find_all(["th","td"])
#     if len(cells) >= 8:
#         cells = [cells[0], cells[2], cells[3], cells[5], cells[6], cells[7]]

#     record = {}
#     cell_index = 0
#     column_index = 0
#     has_no = row.find("th", scope="row") is not None

#     while column_index < len(columns):
#         column = columns[column_index]
#         # 如果这一列有 rowspan 缓存
#         if column in span_cache:
#             record[column] = span_cache[column]["value"]
#             span_cache[column]["remain"] -= 1
#             if span_cache[column]["remain"] == 0:
#                 del span_cache[column]
#             column_index += 1
#             continue
#         # 如果还有真实cell
#         if cell_index < len(cells):
#             cell = cells[cell_index]
#             cell_index += 1
#             for sup in cell.find_all("sup"):
#                 sup.decompose()
#             if column == "Party":
#                value = cell.get_text(" ", strip=True)
#                if column == "Party":
#                 print(record.get("No."), value)
#             else:
#                 value = cell.get_text(" ", strip=True)
#             record[column] = value
#             rowspan = int(cell.get("rowspan",1))
#             if rowspan > 1:
#                 span_cache[column]={
#                     "value":value,
#                     "remain":rowspan-1
#                 }
#         else:
#             record[column]=""
#         column_index += 1
#     records.append(record)

# # 合并 election 多次出现
# clean_records= []
# for record in records:
#     # 空行过滤
#     if record["No."] == "":
#         continue
#     clean_records.append(record)

# merged_records = {}
# for record in clean_records:
#     no = record["No."]
#     if no not in merged_records:
#         merged_records[no] = record
#         if isinstance(record["Party"], list):
#             merged_records[no]["Party"] = record["Party"]
#         else:
#             merged_records[no]["Party"] = [record["Party"]]
#         merged_records[no]["Election"] = [record["Election"]]
#         merged_records[no]["Vice President"] = [record["Vice President"]]
#     else:
#         current = merged_records[no]
#         if record["Party"]:
#             if isinstance(record["Party"], list):
#                 current["Party"].extend(record["Party"])
#             else:
#                 current["Party"].append(record["Party"])
#         if record["Election"]:
#             current["Election"].append(record["Election"])
#         if record["Vice President"]:
#             current["Vice President"].append(record["Vice President"])
# clean_records = list(merged_records.values())

# for record in clean_records:
#     # 去重
#     # Party拆分
#     party_list = []
#     for party in record["Party"]:
#         if isinstance(party, list):
#             party_list.extend(party)
#         else:
#             party_list.append(party)
#     record["Party"] = list(dict.fromkeys(party_list))
#     record["Election"] = list(dict.fromkeys(record["Election"]))
#     record["Vice President"] = list(dict.fromkeys(record["Vice President"]))

#     # 如果只有一个，改回字符串
#     if len(record["Party"]) == 1:
#         record["Party"] = record["Party"][0]
#     if len(record["Election"]) == 1:
#         record["Election"] = record["Election"][0]
#     if len(record["Vice President"]) == 1:
#         record["Vice President"] = record["Vice President"][0]


# # 保存 JSON
# with open("presidents.json", "w", encoding="utf-8") as f:
#     json.dump(clean_records, f, indent=4, ensure_ascii=False)

# print(clean_records[:10])


import requests
from bs4 import BeautifulSoup
import json

# 获取网页
url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'

headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
print(response.status_code)

# 如果请求失败，直接抛出异常
response.raise_for_status()

content = response.content
soup = BeautifulSoup(content, 'html.parser')

print(soup.title)


# 查看网页一共有几张表格，确认第几个表格是需要的
tables = soup.find_all('table')

print(len(tables))

for i, table in enumerate(tables):
    print(i, table.get_text(" ", strip=True)[:100])


# 已确认总统表格是第一个表格
table = tables[0]


# 提取表头，同时删除上标
header_row = table.find("tr")

header_names = []

for th in header_row.find_all('th'):

    for sup in th.find_all("sup"):
        sup.decompose()

    header_names.append(
        th.get_text(" ", strip=True)
    )

print(header_names)


# 最终需要保存的字段
columns = [
    'No.',
    'Name (birth–death)',
    'Term',
    'Party',
    'Election',
    'Vice President'
]


# HTML实际存在的8个列位置
# Portrait和Party Color最终不保存，
# 但处理rowspan时必须保留它们的位置
full_columns = [
    'No.',
    'Portrait',
    'Name (birth–death)',
    'Term',
    'Party Color',
    'Party',
    'Election',
    'Vice President'
]


# 清理单元格文字
def clean_cell_text(cell):

    # 删除脚注
    for sup in cell.find_all("sup"):
        sup.decompose()

    value = cell.get_text(" ", strip=True)

    # 替换不间断空格
    value = value.replace("\xa0", " ")

    # 合并多余空格
    value = " ".join(value.split())

    # Democratic- Republican
    # 恢复成 Democratic-Republican
    value = value.replace("- ", "-")

    return value


# 保存跨行单元格
# key是实际列的位置，例如0、1、2……
span_cache = {}

records = []


# 只读取tbody里面的数据行
tbody = table.find("tbody")

if tbody:
    rows = tbody.find_all("tr", recursive=False)
else:
    rows = table.find_all("tr")[1:]


for row in rows:

    # recursive=False避免读取单元格内部可能存在的其他表格
    cells = row.find_all(
        ["th", "td"],
        recursive=False
    )

    # 当前网页视觉上的完整8列
    # 用None区分“还没有填入”和“单元格本身是空字符串”
    visual_row = [None] * len(full_columns)


    # ===================================
    # 1. 先把上一行留下的rowspan填入当前行
    # ===================================

    for column_index in list(span_cache.keys()):

        visual_row[column_index] = (
            span_cache[column_index]["value"]
        )

        span_cache[column_index]["remain"] -= 1

        if span_cache[column_index]["remain"] == 0:
            del span_cache[column_index]


    # ===================================
    # 2. 把当前HTML行中的真实单元格放入空位置
    # ===================================

    column_index = 0

    for cell in cells:

        # 跳过已经被rowspan占据的位置
        while (
            column_index < len(full_columns)
            and visual_row[column_index] is not None
        ):
            column_index += 1


        if column_index >= len(full_columns):
            break


        value = clean_cell_text(cell)


        rowspan_value = cell.get("rowspan", 1)
        colspan_value = cell.get("colspan", 1)

        # 防止网页中属性为空字符串
        rowspan = int(rowspan_value or 1)
        colspan = int(colspan_value or 1)


        # 一个单元格可能通过colspan占多列
        for offset in range(colspan):

            current_index = column_index + offset

            if current_index >= len(full_columns):
                break

            visual_row[current_index] = value


            # 保存需要延续到后面行的内容
            if rowspan > 1:

                span_cache[current_index] = {
                    "value": value,
                    "remain": rowspan - 1
                }


        column_index += colspan


    # 没有内容的位置转换为空字符串
    visual_row = [
        value if value is not None else ""
        for value in visual_row
    ]


    # ===================================
    # 3. 从完整8列中提取真正需要保存的6列
    # ===================================

    record = {
        'No.': visual_row[0],
        'Name (birth–death)': visual_row[2],
        'Term': visual_row[3],
        'Party': visual_row[5],
        'Election': visual_row[6],
        'Vice President': visual_row[7]
    }

    records.append(record)


# ===================================
# 过滤无效行
# ===================================

clean_records = []

for record in records:

    if record["No."] == "":
        continue

    clean_records.append(record)


# ===================================
# 合并同一总统对应的多行
# ===================================

merged_records = {}

for record in clean_records:

    no = record["No."]


    if no not in merged_records:

        merged_records[no] = {
            "No.": record["No."],
            "Name (birth–death)": record[
                "Name (birth–death)"
            ],
            "Term": record["Term"],
            "Party": [],
            "Election": [],
            "Vice President": []
        }


    current = merged_records[no]


    # Party、Election和Vice President都可能有多个值
    for column in [
        "Party",
        "Election",
        "Vice President"
    ]:

        value = record[column]

        # 排除空字符串，同时避免重复
        if value and value not in current[column]:
            current[column].append(value)


clean_records = list(merged_records.values())


# ===================================
# 只有一个值时，把列表还原成字符串
# ===================================

for record in clean_records:

    for column in [
        "Party",
        "Election",
        "Vice President"
    ]:

        if len(record[column]) == 1:
            record[column] = record[column][0]

        elif len(record[column]) == 0:
            record[column] = ""


# ===================================
# 保存JSON
# ===================================

with open(
    "presidents.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        clean_records,
        f,
        indent=4,
        ensure_ascii=False
    )


print(clean_records[:10])






