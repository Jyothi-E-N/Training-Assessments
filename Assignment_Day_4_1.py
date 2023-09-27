# Assignment 4.1

def sum(*nums):
    res = 0
    print(nums)
    
    for num in nums:
        res += num
    
    return res

def average_num(*nums):
    sum_nums = sum(*nums)
    return sum_nums/len(nums)

average_num(1,2,3)
