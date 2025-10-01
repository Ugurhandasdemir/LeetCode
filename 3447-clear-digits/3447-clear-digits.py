class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """

        last_alpha = []
        for element in s :
            if element.isdigit():
                if last_alpha:
                    last_alpha.pop()
            else:
                last_alpha.append(element)

        return "".join(last_alpha)
                