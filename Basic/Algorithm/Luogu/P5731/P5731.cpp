//
// Created by hosibosi on 2021/4/2.
//

#include <iostream>
#include <cstring>

int P5731() {
    int arrayNum, row = 0, col = 0, loop_time = 0, circle_time = 0;
    std::cin >> arrayNum;
    int array[arrayNum][arrayNum];
    std::memset(array, 0, sizeof array);
    while (loop_time < arrayNum*arrayNum){
        while (col < arrayNum - circle_time){
            array[row][col] = ++loop_time;
            col++;
        }
        col--;
        row++;
        while (row < arrayNum - circle_time){
            array[row][col] = ++loop_time;
            row++;
        }
        row--;
        while (col > circle_time){
            col--;
            array[row][col] = ++ loop_time;
        }
        ++circle_time;
        while (row > circle_time){
            row --;
            array[row][col] = ++ loop_time;
        }
        col++;
    }
    for (int i = 0; i < arrayNum; ++i) {
        for (int j = 0; j < arrayNum; ++j) {
            if (array[i][j] < 10){
                std::printf("%3d", array[i][j] );
            } else std::printf("%3d", array[i][j]);
        }
        std:: cout << std::endl;
    }
}`