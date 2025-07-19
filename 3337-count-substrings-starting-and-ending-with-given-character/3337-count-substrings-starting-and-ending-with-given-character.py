class Solution(object):
    def countSubstrings(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: int
        """
        answer = 1
        count = 0
        for i in range(len(s)):
            if s[i]==c:
                count+=1
        
        answer = (count*(count+1))/2
        
        if count ==0:
            answer = 0

        return answer


        