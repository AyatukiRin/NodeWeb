# m, n = input().split()
# for position, number in enumerate(n):
#     if number != '0':
#         print(number+'*'+m+'^'+str(len(n) - position - 1), end="+")


m, n = input().split()
result_str = ''
for position, number in enumerate(n):
    if number != '0':
        result_str += number+'*'+m+'^'+str(len(n) - position - 1) + '+'
print(result_str[:-1])