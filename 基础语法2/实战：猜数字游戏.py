"""
演示 if elif else  的  实战  猜数字游戏
"""
# 构建一个随机的数字变量 1-10
import random
num = random.randint(1, 10)

guess_num = int(input("输入你要猜的数字："))

# 通过if 判断语句进行数字的猜测
if guess_num == num:
    print("恭喜你猜中了！")
else:
    if guess_num > num:
        print("猜大了！")
    else:
        print("猜小了")

    guess_num = int(input("再次输入你要猜的数字："))

    if guess_num == num:
        print("恭喜你第二次猜中了！")
    else:
        if guess_num > num:
            print("猜大了！")
        else:
            print("猜小了")
    guess_num = int(input("第三次输入你要猜的数字："))

    if guess_num == num:
        print("恭喜你第三次猜中了！")
    else:
        print("三次机会用完了，没有猜中")
