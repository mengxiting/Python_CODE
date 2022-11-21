"""
演示 while 循环 练习 ：猜数字游戏
"""
import random
num = random.randint(1, 100)

count = 0

# 通过一个布尔类型的变量，做循环是否继续的标记
flag = True
while flag:
    guess_num = int(input("请输入你要猜的数字："))
    count += 1
    if num == guess_num:
        print("猜对了")
        flag = False
    else:
        if num < guess_num:
            print("猜大了")
        else:
            print("猜小了")

print(count)
