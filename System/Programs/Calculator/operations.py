#Importable Code
def add(*nums):
    return sum(nums)

def subtract(*nums):
    nums = list(nums)
    answer = nums[0]
    nums.pop(0)
    for number in nums:
        answer -= number
        
    return answer

def multiply(*nums):
    nums = list(nums)
    answer = nums[0]
    nums.pop(0)
    for numbers in nums:
        answer*=numbers
    
    return answer

def divide(*nums):
    nums = list(nums)
    answer = nums[0]
    nums.pop(0)
    for numbers in nums:
        answer /=numbers

    return answer

def exponent(number, exponent):
    answer = number
    for _ in range(1, exponent):
        answer*=number
    
    return answer