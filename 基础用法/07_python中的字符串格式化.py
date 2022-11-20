# 通过占位的形式，完成拼接
name = "深圳职业技术学院"
message = "上大专来:%s" % name
print(message)
# 通过占位的形式，完成数字和字符串的拼接
class_num = 74
avg_salary = 17783
message = "Python大数据学科，广东%s期，毕业平均工资：%s" % (class_num, avg_salary)
print(message)

name = "深圳职业技术学院"
found_time = 1993
settle = 50.3
message = "%s, 成立时间：%d, 总资产：%f" % (name, found_time, settle)
print(message)

num = 11
num2 = 11.345
print("数字11限制宽度5，结果：%5d" % num)
print("数字11限制宽度1，结果：%1d" % num)
print("数字11.345限制宽度7，小数精度2，结果：%7.2f" % num2)
print("数字11.345不限制宽度，小数精度2，结果：%.2f" % num2)
