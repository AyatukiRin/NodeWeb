"""
in:
4 5
0 s 0 1
0 0 1 0
0 1 1 0
0 0 1 g
0 0 0 0

out:
9
"""

row, col = map(int, input().split())
map_col2row = {}
s_col = 0
s_row = 0
g_col = 0
g_row = 0
for i in reversed(range(col)):
    map_col2row[i] = list(input().split())
    for v in map_col2row[i]:
        if v == 's':
            s_col = i
            s_row = map_col2row[i].index(v)
        elif v == 'g':
            g_col = i
            g_row = map_col2row[i].index(v)
print(s_col, s_row)
print(g_col, g_row)
move_command_list = ['LEFT', 'DOWN', 'RIGHT', 'UP']


