class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        temp = 0
        answer = []

        for num in nums:

            if num==1:
                temp += 1
            else:
                answer.append(temp)
                temp=0
            answer.append(temp)
        
        return max(answer)