class Solution(object):
    def findGCD(self, nums):
        mn = min(nums)
        mx = max(nums)

        for i in range(1,mx+1):
            if mn%i == 0 and mx%i == 0:
                answer = i

        return answer



        