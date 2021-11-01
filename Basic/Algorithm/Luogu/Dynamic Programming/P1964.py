# 2,4 RE
"""
20 3
63 0 64 yinshifen
1 0 1 men
1 0 64 yinshifen
"""
maxSpace = 21
usedSpace, saleNum = map(int, input().split())
saleDic = {}
for i in range(saleNum):
    elementList = list(input().split())
    name = elementList[-1]
    valueList = list(map(int, elementList[:-1]))
    if name in saleDic.keys():
        saleDic[name][0] += valueList[0]
    else:
        saleDic[name] = valueList
resultList = []
for j in range(maxSpace - usedSpace):
    maxValue = 0
    initValue = 0
    flagDic = {}
    for key in saleDic.keys():
        objNum, objValue, objMaxNum = saleDic[key]
        if objValue == 0:
            continue
        if objNum >= objMaxNum:
            maxValue = max(initValue, objMaxNum * objValue)
            if maxValue == objMaxNum * objValue:
                flagDic.clear()
                flagDic[key] = objMaxNum
            initValue = maxValue
        else:
            maxValue = max(initValue, objValue * objNum)
            if maxValue == objNum * objValue:
                flagDic.clear()
                flagDic[key] = objNum
            initValue = maxValue
    if len(flagDic) != 0:
        saleDic[list(flagDic.keys())[0]][0] -= list(flagDic.values())[0]
    resultList.append(maxValue)
result = 0
for num in resultList:
    result += num
print(result)
