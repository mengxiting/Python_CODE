"""
演示if elif else的练习： 猜猜心里数
"""
# 定义一个变量数字
num = 10

# 通过键盘输入获取猜想的数字， 通过多次的if 和 elif 的组合进行猜想比较
if int(input("请输入第一次猜想的数字：")) == num:
    print("恭喜第一次就猜对了！")
elif int(input("不对，再猜一次：")) == num:
    print("恭喜你猜对啦！")
elif int(input("不对，最后再猜一次：")) == num:
    print("恭喜你猜对啦！")
else:
    print("Sorry,全部猜错了，我想的是：10")
