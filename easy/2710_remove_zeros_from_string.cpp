#include <string>
#include <stdio.h>

class Solution {
public:
    //std::string removeTrailingZeros(std::string num) {
    //    int len = num.size();
    //    int i = len - 1;
    //    while (num.at(i) == '0') {
    //        i--;
    //        num.pop_back();
    //    }
    //    return num;
    //}

    std::string removeTrailingZeros(std::string num) {
        while (num.back() == '0' && num.size()) {
            num.pop_back();
        }
        return num;
    }
};
