#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>

const int maxSpace = 21;
long result = 0;

int main() {
    std::map<std::string, std::vector<int>> saleDic;
    std::vector<std::string> TypeList;
    std::string name;
    int usedSpace, saleNum, objNum, objValue, objMaxNum;

    std::cin >> usedSpace >> saleNum;
    while (saleNum--) {
        std::cin >> objNum >> objValue >> objMaxNum >> name;
        if (std::find(TypeList.begin(), TypeList.end(), name) == TypeList.end()) {
            TypeList.emplace_back(name);
            saleDic[name].push_back(objNum);
            saleDic[name].push_back(objValue);
            saleDic[name].push_back(objMaxNum);
        } else {
            saleDic[name][0] = saleDic[name][0] + objNum;
        }
    }
    for (int i = 0; i < maxSpace - usedSpace; ++i) {
        std::pair<std::string, int> usedNumList;
        int maxValue = 0;
        int initValue = 0;
        for (const std::string &type : TypeList) {
            int &Num = saleDic[type][0];
            int &value = saleDic[type][1];
            int &maxNum = saleDic[type][2];
            if (value == 0) continue;
            if (Num >= maxNum) {
                maxValue = std::max(initValue, maxNum * value);
                if (maxValue == maxNum * value) {
                    usedNumList.first = type;
                    usedNumList.second = maxNum;
                }
                initValue = maxValue;
            } else {
                maxValue = std::max(initValue, Num * value);
                if (maxValue == Num * value) {
                    usedNumList.first = type;
                    usedNumList.second = Num;
                }
                initValue = maxValue;
            }
        }
        result = result + maxValue;
        if (!usedNumList.first.empty())
            saleDic[usedNumList.first][0] = saleDic[usedNumList.first][0] - usedNumList.second;
    }
    std::cout << result;
}