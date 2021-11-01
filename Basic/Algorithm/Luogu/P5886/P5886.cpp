#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>

int P5886(){ // 完全不清楚到底是啥情况最后的检查点过不了
    int questionNum, answerNum, assumeNum, loop = 0, position;
    std::vector<int> vec1;
    int numArray[1000005];
    std::cin >> questionNum >> answerNum >> assumeNum;
    for (int i = 0; i < questionNum; ++i) {
        std::cin >> loop;
        while (loop--){
            std::cin >> position;
            numArray[position]++;
        }
    }
    for (int i = 1; i <= questionNum; ++i) {
        if (numArray[i] == assumeNum)
            vec1.push_back(i);
    }
    std::cout << vec1.size() << std::endl;
    for (int num: vec1)
        std::cout << num << ' ';
    std::cout << std::endl;
}