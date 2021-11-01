//
// Created by hosibosi on 2021/3/28.
//

#include <iostream>
int main()
{
    char c;
    std::cin >> c;
    c = static_cast<char>(c - 32);
    std::cout << c;
}