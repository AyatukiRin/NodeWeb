cow_num, bookshelf_height = map(int, input().split())
cow_height_list = []
for loop_time in range(cow_num):
    cow_height_list.append(int(input()))
cow_height_list.sort(reverse=True)
cow_tower_height = 0
least_cow_num = 0
for height in cow_height_list:
    cow_tower_height += height
    least_cow_num += 1
    if cow_tower_height >= bookshelf_height:
        print(least_cow_num)
        break
