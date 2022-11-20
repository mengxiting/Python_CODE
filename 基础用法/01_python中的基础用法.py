"""
演示python中的字面量，转义字符，注释
"""

#可以输出数字
print(520)
print(98.5)

# 可以输出字符串
print('Hello World')
print("Hello World")

# 含有运算符的表达式
print(3+1)

# 将数据输入到文件中，注意点 ： 1.所指定的盘符存在  2. 使用 file = fp ;
# fp=open('D:/text.txt','a+')
# print('Hello World',file=fp)
# fp.close()

# 进行换行输出（输出内容在一行中）
print('Hello','World','Python')

# 转义字符
print('Hello\nWorld')
print('Hello\tWorld')
# \b 退格符
print('Hello\bWorld')
# \r 回车符
print('Hello\rWorld')
print('\'Hello\'')
print('http:\\\\www.baidu.com')
print('\"Hello\"')


