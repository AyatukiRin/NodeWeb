questionNum, answerNum, assumeNum = map(int, input().split())
answerList = [0 for x in range(answerNum)]
for loop in range(questionNum):
    for position in list(map(int, input().split()[1:])):
        answerList[position - 1] += 1
resultList = []
for position in range(answerNum):
    if answerList[position] == assumeNum:
        resultList.append(position + 1)
resultList.sort()
print(len(resultList))
for el in resultList:
    print(el, end=' ')