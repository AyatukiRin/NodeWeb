square_length = int(input())
count = 0
for row in range(square_length):
    for col in range(1, square_length + 1):
        num = col + row * square_length
        if num < 10:
            num = '0{}'.format(num)
        num = str(num)
        print(num, end='')
    print('')
print('\n', end='')
for row in range(square_length):
    for col in range(1, square_length + 1):
        if col >= square_length - row:
            num = col + row * square_length - count
            if num < 10:
                num = '0' + str(num)
            num = str(num)
            print(num, end='')
        else:
            print("  ", end='')
            count += 1
    print('')
