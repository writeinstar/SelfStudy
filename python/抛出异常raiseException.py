__author__ = 'devlmj'

def input_password():

    pwd = input("Please input password: ")

    if len(pwd) >= 8:
        return pwd

    print("throw a exception")
    #创建异常对象 ex， 把错误信息作为参数
    ex = Exception("password lengh is less than 8")
    #抛出异常对象
    raise ex

try:
    print(input_password())

except Exception as result:
    print(result)