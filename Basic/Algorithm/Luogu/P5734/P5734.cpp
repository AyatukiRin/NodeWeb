//
// Created by hosibosi on 2021/4/2.
//

//
// Created by hosibosi on 2021/4/2.
//

#include <iostream>
#include <cstring>

int main() {
    int loop_time;
    std::string str;
    std::cin >> loop_time >> str;
    for (int i = 0; i < loop_time; ++i) {
        int command_num;
        std::cin >> command_num;
        if (command_num == 1){
            std::string str2;
            std::cin >> str2;
            str.append(str2);
            std::cout<< str << std::endl;
        }
        if (command_num == 2){
            int start, end;
            std::cin >> start >> end;
            str = str.substr(start, end);
            std::cout << str << std::endl;
        }
        if (command_num == 3){
            int position;
            std::string str3;
            std::cin >> position >> str3;
            str = str.insert(position, str3);
            std::cout << str << std::endl;
        }
        if (command_num == 4){
            std::string str4;
            std::cin >> str4;
            std::cout << int(str.find(str4)) << std::endl;
        }
    }
}