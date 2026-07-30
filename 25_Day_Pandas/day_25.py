import pandas as pd
import numpy as np

nums = [1,2,3,4,5]
s = pd.Series(nums)
print(s)
s = pd.Series(nums, index=[1,2,3,4,5])
print(s)

df = pd.read_csv(r"D:\Study\30-Days-of-Python-ssy\30-Days-Of-Python\data\weight-height.csv")
print(df.head())
print(df.shape)
print(df.columns)

heights = df['Height'] # this is now a series
weights = df['Weight'] # this is now a series
print(heights)


# 导入pandas包
import pandas as pd
# 导入numpy包
import numpy as np
# 数据
data = [
    {"Name": "张三", "Country":"中国", "City":"上海"},
    {"Name": "李四", "Country":"中国", "City":"北京"},
    {"Name": "王五", "Country":"中国", "City":"广州"}]
# 创建一个数据框
df = pd.DataFrame(data)
print(df)
weights = [74, 78, 69]
df['Weight'] = weights
heights = [173, 175, 169]
df['Height'] = heights
print(df)
df.iloc[1, 0] = '阿七'
print('修改后的数据：\n', df)
# 添加身高、体重和BMI列
df['BMI'] = np.round(df['Weight'] / ((df['Height'] * 0.01) ** 2), 2) # 保留两位小数
print(df)



# Exercises: Day 25
print('\n# 1')
import pandas as pd
df = pd.read_csv(r"D:\Study\30-Days-of-Python-ssy\30-Days-Of-Python\data\hacker_news.csv")

print('\n# 2')
print(df.head())

print('\n# 3')
print(df.tail())

print('\n# 4')
titles = df["title"]
print(titles)

print('\n# 5')
print(df.describe())
df_python = df[df["title"].str.contains("python")]
print(df_python)
df_JavaScript = df[df["title"].str.contains("JavaScript")]
print(df_JavaScript)

print('\n# 6')
# 获取第二行和第四行从第二列到第四列的数据
df_choose = df.iloc[[1, 3], 1:4]
print(df_choose)

print('\n# 7')
# 按评论数进行排序
df_order = df.sort_values(by="num_comments", ascending=False)
print(df_order.head(10))