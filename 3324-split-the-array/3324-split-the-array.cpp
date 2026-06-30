class Solution {
public:
    bool isPossibleToSplit(vector<int>& nums) {
        sort(nums.begin(), nums.end());  
        int old = nums[0];
        int count = 1;

        for(int i=0; i<nums.size(); i++){
            cout<< nums[i];
        }
        
        for (int i=1; i<nums.size(); i++){
            if(nums[i]==old){
                count+=1;
            }
            else{
                count = 1;
            }

            if(count==3)
                return false;
            

            old = nums[i];
        }

        return true;

    }
};