"""
演示循环语句中的中断控制 ： break 和 continue
"""

# # 演示循环中断语句 continue
# for i in range(5):
#     print("语句1")
#     continue # 跳过语句2 执行下一次
#     print("语句2")

# 演示循环中断语句 break
for i in range(101):
    print("语句1")
    break # 直接终止循环
    print("语句2")

print("语句3")
