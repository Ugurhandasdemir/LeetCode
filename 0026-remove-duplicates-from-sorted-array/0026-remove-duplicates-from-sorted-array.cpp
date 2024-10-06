class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.empty()) return 0;

        stack<int> answer;
        int count = 0;

        answer.push(nums[0]); 
        for(int i = 1; i < nums.size(); i++){
            if(answer.top() < nums[i]){
                answer.push(nums[i]);
            }
            else{
                count++;
            }
        }

        int k = answer.size();
        
        for (int i = k - 1; i >= 0; i--) {
            nums[i] = answer.top();
            answer.pop();
        }

        return k;
    }
};