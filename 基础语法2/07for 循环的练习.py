"""
演示 for 循环 的 练习 数一数字符串中有多少个 a
"""
# 统计以下字符串有多少个字母a
name = "itheima is a brand of itcast"
# 设一个计数器，记录a的个数
count = 0

for x in name:
    if x == 'a':
        count += 1

print(f"itheima is a brand of itcast中有{count}个字母a")
