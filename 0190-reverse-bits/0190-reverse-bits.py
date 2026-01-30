class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        answer = format(n, "032b")   
        answer = answer[::-1]        
        answer = int(answer, 2)      

        return answer
