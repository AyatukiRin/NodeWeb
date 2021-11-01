//
// Created by hosibosi on 2021/4/3.
//
#include <iostream>


int P5743(){
    int total_day, lastOne = 1;
    std::cin >> total_day;
    for (int i = 0; i <total_day - 1 ; ++i) {
        lastOne = (lastOne + 1) * 2;
    }
    std:: cout << lastOne;
}
