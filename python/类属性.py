__author__ = 'devlmj'
class Tool(object):

    count = 0

    def __init__(self,name):
        self.name = name

        Tool.count += 1


tool1 = Tool("knife")

print(Tool.count)
print(tool1.count) # 不推荐使用