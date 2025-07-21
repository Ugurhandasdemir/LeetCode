class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = []

        for num in nums:
            digits = []

            if num == 0:
                digits.append(9)
            while num >0 :
                digits.append(num%10)
                num = num//10
            answer.extend(digits[::-1])  
        
        return answer
        