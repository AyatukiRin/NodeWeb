n, m, bombing_time, key_point_num = map(int, input().split())
bombing_range_x = {}
bombing_range_y = {}
result_dict = {}
for i in range(bombing_time):
    x1, y1, x2, y2 = map(int, input().split())
    bombing_range_x[i] = [min(x1, x2), max(x1, x2) + 1]
    bombing_range_y[i] = [min(y1, y2), max(y1, y2) + 1]
for i in range(key_point_num):
    position_x, position_y = map(int, input().split())
    result_bool = 'N'
    result_time = 0
    final_time = 0
    for j in range(bombing_time):
        if position_x in range(bombing_range_x[j][0], bombing_range_x[j][1]) \
                and position_y in range(bombing_range_y[j][0], bombing_range_y[j][1]):
            result_bool = 'Y'
            result_time += 1
            final_time = j + 1
    result_dict[i] = [result_bool, result_time, final_time]
for i in range(key_point_num):
    for value in result_dict[i]:
        if value == 0:
            continue
        else:
            print(value, end=' ')
    print('')