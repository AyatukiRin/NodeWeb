i = int(input())
lt = []
for k in range(i):
    lt.append(int(input()))
for begin_num in lt:
    if begin_num % 2 == 0:
        print("pb wins")
    else:
        print("zs wins")