"""
演示 for 嵌套循环的练习：  九九乘法表
"""

# 设置外层循环的变量控制行数
for i in range(1, 10):
    # 设置内层循环的变量控制每一行的数据
    for j in range(1, i+1):
        print(f"{j}*{i}={j*i}\t", end=' ')
    # 外层循环可以通过 print输出一个回车符
    print()

