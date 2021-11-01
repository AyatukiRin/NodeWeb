"""
这里使用了康托展开来计算，python库中自带全排列来求出字典序
"""


def check(num_for_check):
    checked_list = list(filter(lambda x: x < num_for_check, list_num))
    list_num.remove(num_for_check)
    return checked_list


def factorial(num_position):
    factorial_result = 1
    for i in range(1, girl_num - num_position):
        factorial_result *= i
    return factorial_result


girl_num = int(input())
list_num = list(input())
final_result = 0
for position, num in enumerate(list_num[:]):
    checked_num_list = check(num)
    final_result += len(checked_num_list) * factorial(position)
final_result += 1
print(final_result)

# import itertools  # 一个神奇的库，用来弄全排列
#
# n = int(input())  # 输入
# re = list(input())  # 输入
# l = list(itertools.permutations(re, n))  # 全排列函数
# l = sorted(l)  # 排序
# for i in range(len(l)):
#     if list(l[i]) == re:  # 匹配就输出
#         print(i + 1)
#         break
