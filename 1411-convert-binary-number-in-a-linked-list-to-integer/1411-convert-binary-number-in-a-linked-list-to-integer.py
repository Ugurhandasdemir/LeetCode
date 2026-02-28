class Solution(object):
    def getDecimalValue(self, head):
        stack = []
        temp = head
        
        while temp is not None:
            stack.append(temp.val)
            temp = temp.next
        
        sonuc = 0
        us = 0
        
        while len(stack) > 0:
            eleman = stack.pop()
            sonuc = sonuc + eleman * (2 ** us)
            us = us + 1
        
        return sonuc