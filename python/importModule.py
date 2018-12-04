__author__ = 'devlmj'

import random


def say_hello():
    print("Hello world ")


def main():
    print(__name__)
    print("XiaoMing module")
    say_hello()
if __name__ == "__main__": # importModule 被其他文件导入时，不会执行main，任何没有任何缩进的代码会被执行一遍
    main()

print(random.__file__) # 会被执行，没有缩进
