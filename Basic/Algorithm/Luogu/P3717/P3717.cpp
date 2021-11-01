//
// Created by hosibosi on 2021/3/25.
//

#include <iostream>
#include <vector>
#include <cmath>


int count = 0;
int P3717()
{
    int area, numDetector, radius;
    double distanceIn2P;
    std::cin >> area >> numDetector >> radius;
    std::vector<std::pair<int, int>> detectorPosition;
    for (auto i = 0; i < numDetector; ++i) {
        int dP_x, dP_y;
        std::cin >> dP_x >> dP_y;
        detectorPosition.emplace_back(std::make_pair(dP_x, dP_y));
    }
    for (auto position_x = 1; position_x <= area; ++position_x) {
        for (auto position_y = 1; position_y <= area; ++position_y) {
            for (auto dP : detectorPosition){
                distanceIn2P = sqrt(pow(position_x - dP.first, 2) + pow(position_y - dP.second, 2));
                if (distanceIn2P <= radius){
                    count++;
                    break;
                }
            }
        }

    }
    std::cout<< count << std::endl;
}