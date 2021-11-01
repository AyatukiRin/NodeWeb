//
// Created by hosibosi on 2021/3/29.
//
#include <iostream>
#include <iomanip>
int P7506(){
    double drink;
    int numPerson;
    std::cin >> drink >> numPerson;
    std::cout << std::fixed << std::setprecision(3) << drink / numPerson << '\n' << numPerson * 2 <<std::endl;
}