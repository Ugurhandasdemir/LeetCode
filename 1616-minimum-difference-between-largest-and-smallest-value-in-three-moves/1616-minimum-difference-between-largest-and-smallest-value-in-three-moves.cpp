class Solution {
public:
    int minDifference(vector<int>& nums) {
        int size = nums.size();
        if (size < 5)              // 4 ve altÄ± iÃ§in cevap her zaman 0
            return 0;

        vector<int> max_nums     = nums;
        vector<int> min_nums     = nums;
        vector<int> two_max_nums = nums;
        vector<int> two_min_nums = nums;

        int answer[4];

        sort(max_nums.begin(), max_nums.end(), greater<int>());
        sort(min_nums.begin(), min_nums.end());
        sort(two_max_nums.begin(), two_max_nums.end());   
        sort(two_min_nums.begin(), two_min_nums.end());   

        int min = *min_element(nums.begin(), nums.end());
        int max = *max_element(nums.begin(), nums.end());

        for (int i = 0; i < 3; i++) {
            max_nums[i] = min;     
            min_nums[i] = max;     
        }

        two_max_nums[0]      = two_max_nums[1];
        two_max_nums[size-1] = two_max_nums[size-3];
        two_max_nums[size-2] = two_max_nums[size-3];

        two_min_nums[0]      = two_min_nums[2];
        two_min_nums[1]      = two_min_nums[2];
        two_min_nums[size-1] = two_min_nums[size-2];

        answer[0] = *max_element(max_nums.begin(), max_nums.end()) - *min_element(max_nums.begin(), max_nums.end());
        answer[1] = *max_element(min_nums.begin(), min_nums.end()) - *min_element(min_nums.begin(), min_nums.end());
        answer[2] = *max_element(two_min_nums.begin(), two_min_nums.end()) - *min_element(two_min_nums.begin(), two_min_nums.end());
        answer[3] = *max_element(two_max_nums.begin(), two_max_nums.end()) - *min_element(two_max_nums.begin(), two_max_nums.end());

        return *min_element(answer, answer + 4);
    }
};