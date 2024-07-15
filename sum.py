def summation(nums):
    sum = 0
    for num in nums:
        sum += num
    return sum

nums = [ 5, 12, 23, 1, 16, 19, 120 ]

res = summation(nums)

print(f'Result is {res}')