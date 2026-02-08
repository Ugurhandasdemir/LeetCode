class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        head = len(nums) -1
        tail= 0
        maxx = 0
        nums = sorted(nums)
        for i in range(len(nums)/2):
            summ= nums[tail] + nums[head]
            head = head -1 
            tail = tail +1
            
            if summ > maxx:
                maxx=summ
        return maxx