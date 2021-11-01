from functools import reduce
loop_time = int(input())
print(reduce((lambda a, b: a * b), [num for num in range(1, loop_time + 1)]))
