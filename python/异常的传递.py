__author__ = 'devlmj'

def demo1():
    return int(input("input integer :"))

def demo2():
    return demo1()

try:
    print(demo2())

#在主程序捕获异常
except Exception as result:
    print("Error: %s" %result)