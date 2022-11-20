# 将数字类型转换成字符串
num_str = str(11)
print(type(num_str), num_str)

float_str = str(3.14)
print(type(float_str), num_str)

# 将字符串转换为数字
num = int("11")
print(type(num), num)

num2 = float("3.14")
print(type(num2), num2)

# 错误示例，想要将字符串转换成数字，必须要求字符串内的内容都是数字
# num3 = int("深圳职业技术学院")
# print(type(num3), num3)

# 整数转换成浮点数
float_num = float(11)
print(type(float_num), float_num)

# 浮点数转换成整数
int_num = int(3.14159)
print(type(int_num), int_num)
