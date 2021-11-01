//
// Created by hosibosi on 2021/4/3.
//

#include <iostream>


int P5739(){
    int loop_time = 0, result = 1;
    std::cin >> loop_time;
//    while (loop_time > 0){
//        result = result * loop_time;
//        loop_time--;
//    }
    for (int i = 1; i <= loop_time; ++i) result = result * i;
    std::cout << result;
}