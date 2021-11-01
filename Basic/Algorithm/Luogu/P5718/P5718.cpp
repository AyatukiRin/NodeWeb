//
// Created by hosibosi on 2021/3/30.
//

#include <iostream>
#include <vector>
#include <algorithm>

//int main(){
//    int n;
//    std::cin >> n;
//    std::vector<int> vec;
//    for (int i = 0; i < n; ++i) {
//        int num;
//        std::cin >> num;
//        vec.emplace_back(num);
//    }
//    std::cout << *std::min_element(vec.begin(), vec.end());
//}
int main(){
    int loop_time;
    std::cin >> loop_time;
    std::vector<int> vec;
    for (int i = 0; i < loop_time; ++i) {
        int num;
        std::cin >> num;
        vec.emplace_back(num);
    }
    int min_num = vec[0];
    for (int i = 1; i < vec.size(); ++i) {
        min_num = std::min(vec[i], min_num);
    }
    std::cout<< min_num;
}