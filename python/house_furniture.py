__author__ = 'devlmj'
class HouseItem:
    def __init__(self, name ,area):
        self.name = name
        self.area = area

    def __str__(self):
        return "%s occupy %.2f"%(self.name, self.area)

class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        #Python 能够自动将一对括号中的代码链接在一起
        return ("House type : %s\narea: %.2f [free area : %.2f]\nfurniture: %s"
                %(self.house_type, self.area, self.free_area, self.item_list))

    def add_item(self, item):
        print("add %s"% item)
        if item.area > self.free_area:
            print("%s is too big,can't be put into house"%item.name)
            return
        self.item_list.append(item.name)
        self.free_area -= item.area


bed = HouseItem("bed", 4)
wardrobe = HouseItem("wardrobe", 2)
table = HouseItem("table",150)

print(bed)
# print(wardrobe)
# print(table)

my_home = House("kaksio", 60)
print(my_home)

my_home.add_item(bed)
my_home.add_item(wardrobe)
my_home.add_item((table))

print(my_home)