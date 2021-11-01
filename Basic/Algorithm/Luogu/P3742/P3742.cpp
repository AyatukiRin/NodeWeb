//
// Created by hosibosi on 2021/3/24.
//
//
// Created by hosibosi on 2021/3/24.
//
#include <iostream>


int P3742()
{
    int charLength;
    std:: string x, z;
    std::cin >> charLength >> x >> z;
    for (int i = 0; i < charLength; ++i)
    {
        if (x[i] < z[i])
        {
            std::cout << -1 << std::endl;
            return 0;
        }
    }
    std::cout << z << std::endl;
}