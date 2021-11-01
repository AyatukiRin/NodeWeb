"""
给定 x, k ，求满足 x + y = x | y 的第 k 小的正整数 y 。 | 是二进制的或(or)运算，例如 3 | 5 = 7。

比如当 x=5，k=1时返回 2，因为5+1=6 不等于 5|1=5，而 5+2=7 等于 5 | 2 = 7。

"""

x, k = map(int, input().split())
binary_x = list(bin(x).replace('0b', ''))
binary_k = list(bin(k).replace('0b', ''))
binary_k_position = len(binary_k) - 1
binary_x_position = len(binary_x) - 1
for binary_x_num in reversed(binary_x):
    if binary_x_num == '0':
        binary_x[binary_x_position] = binary_k[binary_k_position]
        binary_k_position -= 1
        binary_x_position -= 1
    else:
        binary_x_position -= 1
binary_x = binary_x + binary_k[:-len(binary_x)]
final_num = ''
for num in binary_x:
    final_num += num
y = int(final_num, 2) - x
print(y)
