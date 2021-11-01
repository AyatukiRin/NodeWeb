total_mana, skill_num, boss_life = map(int, input().split())
used_skill_list = []
for sequence in range(skill_num):
    cost, damage = map(int, input().split())
    if (not cost and damage) or (total_mana//cost) * damage >= boss_life:
        used_skill_list.append(sequence + 1)
if used_skill_list:
    for i in used_skill_list:
        print(i, end=" ")
else:
    print(-1)