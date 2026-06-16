class Solution {
public:
    int minPairSum(vector<int>& nums) {
        sort(nums.begin(), nums.end(),greater<int>());
        vector<int> sum(nums.size()/2,0);

        for(int i=0;i<(nums.size()/2);i++){
            sum[i] = nums[i] + nums[nums.size()-i-1];
        }
        int answer = *max_element(sum.begin(),sum.end());
        return answer;
    }
};