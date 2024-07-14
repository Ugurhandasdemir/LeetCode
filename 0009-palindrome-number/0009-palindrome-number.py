class Solution(object):
    def isPalindrome(self, x):
        x=str(x)
        revers_num = x[::-1]

        if revers_num == x :
            return True
        else:
            return False



        