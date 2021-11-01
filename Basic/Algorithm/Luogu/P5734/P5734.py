command_time = int(input())
aString = input()
result_list = []
for loop_time in range(command_time):
    command_list = list(input().split())
    if command_list[0] == '1':
        aString += command_list[1]
        result_list.append(aString)
    elif command_list[0] == '2':
        aString = aString[int(command_list[1]):int(command_list[1]) + int(command_list[2])]
        result_list.append(aString)
    elif command_list[0] == '3':
        aString = aString[:int(command_list[1])] + command_list[2] + aString[int(command_list[1]):]
        result_list.append(aString)
    elif command_list[0] == '4':
        result_list.append(aString.find(command_list[1]))
for result in result_list:
    print(result)
