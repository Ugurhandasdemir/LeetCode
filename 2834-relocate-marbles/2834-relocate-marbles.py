class Solution(object):
    def relocateMarbles(self, nums, moveFrom, moveTo):
        """
        :type nums: List[int]
        :type moveFrom: List[int]
        :type moveTo: List[int]
        :rtype: List[int]
        """
        nums = set(nums)
        print(nums)
        for i in range(len(moveFrom)):
            if moveFrom[i] in nums:
                nums.remove(moveFrom[i])
                nums.add(moveTo[i])

        return sorted(nums)
