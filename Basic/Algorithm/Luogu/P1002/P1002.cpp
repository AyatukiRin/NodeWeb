//
// Created by hosibosi on 2021/3/30.
//

//#include <iostream>  这里是用了dfs的错误解法
//#include <vector>
//#include <algorithm>
//int result = 0;
////void dfs_search(std::pair<int, int> &position, std::pair<int, int> &positionB, std::vector<std::pair<int, int>> &listHorse) {
//////    std::pair<int, int> copy = position;
////    int &first = position.first;
////    int &second = position.second;
////    for (int i = 0; i < 2; ++i) {
////        if (i == 0) {
////            if (std::find(listHorse.begin(), listHorse.end(), position) == listHorse.end() && first < positionB.first) {
////                ++first;
////                if (position == positionB){
////                    ++result;
////                    std::cout << result << std::endl;
////                }
////                dfs_search(position, positionB, listHorse);
////                --first;
////            }
////        } else{
////            if (std::find(listHorse.begin(), listHorse.end(), position) == listHorse.end() && second < positionB.second) {
////                ++second;
////                if (position == positionB){
////                    ++result;
////                    std::cout << result << std::endl;
////                }
////
////                dfs_search(position, positionB, listHorse);
////                --second;
////            }
////
////        }
////    }
////}
////
////int main() {
////    std::vector<std::pair<int, int>> listHorse;
////    std::pair<int, int> positionB;
////    std::pair<int, int> positionStart = std::make_pair(0, 0);
////    std::pair<int, int> positionHorse;
////    std::cin >> positionB.first >> positionB.second >> positionHorse.first >> positionHorse.second;
////    listHorse.emplace_back(positionHorse.first - 2, positionHorse.second - 1);
////    listHorse.emplace_back(positionHorse.first - 2, positionHorse.second + 1);
////    listHorse.emplace_back(positionHorse.first - 1, positionHorse.second - 2);
////    listHorse.emplace_back(positionHorse.first - 1, positionHorse.second + 2);
////    listHorse.emplace_back(positionHorse.first + 2, positionHorse.second - 1);
////    listHorse.emplace_back(positionHorse.first + 2, positionHorse.second + 1);
////    listHorse.emplace_back(positionHorse.first + 1, positionHorse.second - 2);
////    listHorse.emplace_back(positionHorse.first + 1, positionHorse.second + 2);
////    listHorse.emplace_back(positionHorse.first, positionHorse.second);
////    dfs_search(positionStart, positionB, listHorse);
////    std::cout << result << std::endl;
////}

#include <iostream>
#include <cstring>
#include <algorithm>

int main() {
    std::pair<int, int> positionB, positionHorse;
    std::cin >> positionB.first >> positionB.second >> positionHorse.first >> positionHorse.second;
    long long positionPawn[positionB.first + 2][positionB.second + 2];
    std::memset(positionPawn, 0, sizeof positionPawn);
    positionPawn[1][1] = 1;
    for (int i = 0; i < 9; ++i) {
        if (positionDangerX[i] + positionHorse.first >= 0 && positionDangerY[i] + positionHorse.second >= 0)
            positionPawn[positionDangerX[i] + positionHorse.first + 1][positionDangerY[i] + positionHorse.second + 1] = -1;
    }
    for (int x = 1; x < positionB.first + 2; ++x) {
        for (int y = 1; y < positionB.second + 2; ++y)
            if (positionPawn[x][y] == -1)
                positionPawn[x][y] = 0;
            else positionPawn[x][y] = std::max(positionPawn[x - 1][y] + positionPawn[x][y - 1], positionPawn[x][y]);
    }
    long a = positionPawn[positionB.first + 1][positionB.second + 1];   // 不加这个的话断点会跑不过来
//    std::cout << positionPawn[positionB.first + 1][positionB.second + 1];
    std::cout << a;
}