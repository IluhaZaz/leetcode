#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        sort(begin(nums), end(nums));
        int curr = 1;

        int l = nums.size();

        if(l == 1){
            if(nums[0] == 1)
                return 2;
            return 1;
        }

        for(int i = 0; i < l; i++){
            if(nums[i] <= 0)
                continue;
            if(nums[i] == nums[i - 1])
                continue;
            if(nums[i] > 0 && nums[i] != curr)
                return curr;
            curr += 1;
        }
        return curr;
    }
};

