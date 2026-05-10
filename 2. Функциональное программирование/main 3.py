from functools import reduce
nums = [0, 1, 2, 3, 4, 5]
sq_num = list(map(lambda x: x**2, nums))
print(sq_num)
total_sum = reduce(lambda acc, x: acc * x, nums)
print(total_sum)