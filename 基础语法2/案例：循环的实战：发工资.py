"""
演示 利用 循环语句 完成 练习： 发工资
"""
# 使用循环对员工依次发工资
# continue 跳过 break 结束

# 账户余额
money = 10000

for i in range(1, 21):
    # 设置一个随机数 记录绩效分
    import random
    num = random.randint(1, 10)
    if num < 5:
        print(f"员工{i},绩效分{num},低于5，不发工资，下一位")
        continue
    if money >= 1000:
        money -= 1000
        print(f"向员工{i}发放工资1000元，账户余额还剩余{money}元")
    else:
        print("工资发完了，下个月领取吧")
        break

