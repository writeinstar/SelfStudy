__author__ = 'devlmj'


try:
    #不能确定正确执行的代码
    num = int(input("Please input a integer: "))
    result = 8/num
    print(result)
except ValueError:
    print("Please input correct integer")

# catch unknown exception 捕获未知异常
except Exception as result:
    print("Unkown error %s:" % result)

else:# 没有异常被执行的代码
    print("try successfully")


finally: #无论是否有异常，都会被执行
    print("Always ")

print("-"*50)