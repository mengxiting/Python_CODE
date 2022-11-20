# 方法1： 使用print 直接输出类型信息
print(type("深圳职业技术学院"))
print(type(666))
print(type(3.14159))
# 方法2： 使用变量存储type（）语句的结果
string_type = type("深圳职业技术学院")
int_type =  type(6666)
float_type = type(3.14159)
print(string_type)
print(int_type)
print(float_type)
# 方法3： 使用type（）， 查看变量中存储的数据类型信息
name = "深圳职业技术学院"
name_type = type(name)
print(name_type)