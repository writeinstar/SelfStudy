__author__ = 'devlmj'
class Tool(object):

    count = 0
    @classmethod
    def show_tool_count(cls):
        print("Tool object count %d" % cls.count)

    def __init__(self,name):
        self.name = name

        Tool.count += 1


tool1 = Tool("knife")

print(Tool.count)
print(tool1.count) # 不推荐使用

Tool.show_tool_count()