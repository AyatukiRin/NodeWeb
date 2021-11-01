"""
def remove_num():   # 可以冒泡但是没有必要
    global change_time
    global train_sequence
    minimal_num = min(train_sequence)
    if train_sequence.index(minimal_num):
        change_time += train_sequence.index(minimal_num)
        train_sequence.remove(minimal_num)
    else:
     train_sequence.remove(minimal_num)


change_time = 0
train_cabin = int(input())
train_sequence = list(map(int, input().split()))
while len(train_sequence) > 1:
    remove_num()
print(change_time)

提示第二个检查点错误

"""

"""

n = int(input())
m = list(map(int, input().split()))
change_time = 0
for i in range(n):
    for j in range(i):
        if m[j] > m[i]:
            change_time += 1
print(change_time)

提示运行时间太长
"""

# python读取多行多值的时候用下面这个函数，洛谷的测试数据是多行多值的
n = int(input())
i = 1
m = []
while i < n:    # 用这个来对给定多行多词的数据一次性接收
    m += list(map(int, input().split()))
    i = len(m)
change_time = 0
while len(m) > 1:
    minimal_num = min(m)
    for i in m:
        if i > minimal_num:
            change_time += 1
        elif i == minimal_num:
            break
    m.remove(minimal_num)
print(change_time)

