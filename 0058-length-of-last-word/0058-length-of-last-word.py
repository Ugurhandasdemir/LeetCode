class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_world = s.strip().split(" ")
        last_world = last_world[-1]
        return len(last_world)