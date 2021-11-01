def check():
    for i in range(char_length):
        if x[i] < z[i]:
            print(-1)
            return None
    print(z)


char_length = int(input())
x = input()
z = input()
check()
