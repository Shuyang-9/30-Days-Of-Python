import numpy as np
print("numpy: ", np.__version__)
# print(dir(np))

python_list = [1,2,3,4,5]
two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]
numpy_array_from_list = np.array(python_list)
print(type(numpy_array_from_list))
print(numpy_array_from_list)

numy_array_from_list2 = np.array(python_list, dtype=float)
print(numy_array_from_list2) # array([1., 2., 3., 4., 5.])

numpy_two_dimensional_list =np.array(two_dimensional_list)
print(numpy_two_dimensional_list)


# Numpy array from tuple
# Creating tuple in Python
python_tuple = (1,2,3,4,5)
print(type (python_tuple)) # <class 'tuple'>
print('python_tuple: ', python_tuple) # python_tuple:  (1, 2, 3, 4, 5)

numpy_array_from_tuple = np.array(python_tuple)
print(type (numpy_array_from_tuple)) # <class 'numpy.ndarray'>
print('numpy_array_from_tuple: ', numpy_array_from_tuple) # numpy_array_from_tuple:  [1 2 3 4 5]

nums = np.array([1, 2, 3, 4, 5])
print(nums)
print('nums的形状: ', nums.shape)
print(numpy_two_dimensional_list)
print('numpy_two_dimensional_list的形状: ', numpy_two_dimensional_list.shape)
three_by_four_array = np.array([[0, 1, 2, 3],
    [4,5,6,7],
    [8,9,10, 11]])
print(three_by_four_array.shape)

int_lists = [-3, -2, -1, 0, 1, 2,3]
int_array = np.array(int_lists)
float_array = np.array(int_lists, dtype=float)

print(int_array)
print(int_array.dtype)
print(float_array)
print(float_array.dtype)

numpy_array_from_list = np.array([1, 2, 3, 4, 5])
two_dimensional_list = np.array([[0, 1, 2],
                              [3, 4, 5],
                              [6, 7, 8]])

print('The size:', numpy_array_from_list.size) # 5
print('The size:', two_dimensional_list.size)  # 9


# 声明
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('原始数组: ', numpy_array_from_list)
print('加法: ', numpy_array_from_list + 2)
print('加法: ', np.add(numpy_array_from_list, 2))

# 声明
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('原始数组: ', numpy_array_from_list)
print('除法: ', numpy_array_from_list / 2)
print('除法: ', np.divide(numpy_array_from_list, 2))

# 声明
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('原始数组: ', numpy_array_from_list)
print('整除: ', numpy_array_from_list // 2)
print('整除: ', np.floor_divide(numpy_array_from_list, 2))

numpy_int_arr = np.array([1,2,3,4], dtype = 'float')
print(numpy_int_arr)

numpy_int_arr = np.array([1., 2., 3., 4.], dtype = 'int')
print(numpy_int_arr)

numpy_int_arr = np.array([-3, -2, 0, 1,2,3], dtype='bool')
print(numpy_int_arr)

numpy_int_arr = np.array([-3, -2, 0, 1, 2, 3])
print(numpy_int_arr.astype('bool'))

two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
first_two_rows_and_columns = two_dimension_array[0:2, 0:2]
print(first_two_rows_and_columns)


numpy_array_from_list = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print('原始数组：', numpy_array_from_list)

# 第一个参数代表：起始位置
# 第二个参数代表：停止位置
# 第三个参数代表：步长
print('第一个参数代表：起始位置')
print('第二个参数代表：停止位置')
print('第三个参数代表：步长')
# 使用正index
ten_first_items = numpy_array_from_list[0:10]
print('前10项：', ten_first_items)
first_five_items = numpy_array_from_list[:5]
print('前5项：', first_five_items)
last_five_items = numpy_array_from_list[5:]
print('后5项：', last_five_items)
# 使用负index
last_five_items = numpy_array_from_list[-5:]
print('后5项：', last_five_items)

every_two_item = numpy_array_from_list[::2]
print('每隔一项：', every_two_item)

# Generate a random float  number
random_float = np.random.randint(3,6)
print(random_float)

# np.random.normal(mu, sigma, size)
normal_array = np.random.normal(79, 15, 80)
print(normal_array)
print(normal_array.mean())
print(normal_array.std())


# creating list using range(starting, stop, step)
lst = range(0, 11, 2)
print(lst)
for i in range(0,11,2):
    print(i)


whole_numbers = np.arange(0, 20, 1)
print(whole_numbers)  # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]
odd_numbers = np.arange(1, 20, 2)
print(odd_numbers)  # [ 1  3  5  7  9 11 13 15 17 19]
even_numbers = np.arange(0, 20, 2)
print(even_numbers)  # [ 0  2  4  6  8 10 12 14 16 18]


print(np.linspace(1.0, 5.0, num=5, endpoint=False))

print(np.logspace(2, 4, num=3))  # [  100.  1000. 10000.]

# to check the size of an array
x = np.array([1,2,3], dtype=np.complex128)
print(x.itemsize)
print(x.size)
print(x.shape)


two_dimension_array = np.array([[1,2,3],[4,55,66], [7,8,9]])
print(two_dimension_array)
print('Column with minimum: ', np.amin(two_dimension_array,axis=0))
print('Column with maximum: ', np.amax(two_dimension_array,axis=0))
print('=== Row ==')
print('Row with minimum: ', np.amin(two_dimension_array,axis=1))
print('Row with maximum: ', np.amax(two_dimension_array,axis=1))

print(np.random.choice(['a', 'e', 'i', 'o', 'u'], size=10))

## Random numbers between [0, 1] of shape 2, 2
rand = np.random.rand(2,2)
print(rand)

from scipy import stats
np_normal_dis = np.random.normal(5, 0.5, 1000) # mean, standard deviation, number of samples
np_normal_dis
## min, max, mean, median, sd
print('min: ', np.min(np_normal_dis))
print('max: ', np.max(np_normal_dis))
print('mean: ', np.mean(np_normal_dis))
print('median: ', np.median(np_normal_dis))
print('mode: ', stats.mode(np_normal_dis))
print('sd: ', np.std(np_normal_dis))

## Linear algebra
### Dot product: product of two arrays
f = np.array([1,2,3])
g = np.array([4,5,6])
### 1*4 + 2*5 + 3*6
print(np.dot(f, g))  # 32

### Matmul: matruc product of two arrays
h = [[1,2],[3,4]]
i = [[5,6],[7,8]]
print(np.matmul(h, i))  # 1*5+2*7 = 19

temp = np.array([1,2,3,4,5])
pressure = temp * 2 + 5
print(pressure)
import matplotlib.pyplot as plt
plt.plot(temp,pressure)
plt.xlabel('Temperature in oC')
plt.ylabel('Pressure in atm')
plt.title('Temperature vs Pressure')
plt.xticks(np.arange(0, 6, step=0.5))
plt.show()

