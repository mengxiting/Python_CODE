"""
演示 while嵌套循环 的练习 ：九九乘法表
"""

# 定义外层循环的控制变量
i = 1

while i <= 9:

    # 定义内层循环的控制变量
    j = 1
    while j <= i:
        # 内层循环的print 语句 不要进行换行end=’‘， 通过\t 制表符进行对齐
        print(f"{j}*{i}={j*i}\t", end=' ')
        j += 1

    i += 1
    print()
