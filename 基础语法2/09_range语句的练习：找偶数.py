"""
演示 range 语句 的练习 ：有几个偶数
"""

# 设置一个计数器，记录偶数的个数
count = 0
for x in range(1, 100):
    if x % 2 == 0:
        count += 1

print("1-100之间偶数有：", count)
