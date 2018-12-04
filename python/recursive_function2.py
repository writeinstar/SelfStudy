__author__ = 'devlmj'
def sum_numbers(num):
    # exit
    if num == 1:
        return 1
    # 数字的累加，num + (1..num-1)
    #假设 sum?numbers 能够正确处理1.。。num-1
    temp = sum_numbers(num-1)
    return num + temp

result = sum_numbers(100)
print(result)