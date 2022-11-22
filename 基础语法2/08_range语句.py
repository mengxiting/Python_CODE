"""
演示python 中的 range()语句的使用
"""

# range 语法一 range(num)
# 从0开始 到 num （不包括num本身）结束
# for x in range(10):
#     print(x)

# range 语法二 range(num1，num2)
# 从num1开始 到 num2 （不包括num2本身）结束，数字间隔是1
# for x in range(5, 10):
#     print(x)

# range 语法三 range(num1，num2,step)  step:表示步长

for x in range(5, 10, 2):
    #  从num1开始 到 num2 （不包括num2本身）结束,数字之间的间隔是2
    print(x)
