class Solution(object):
    def lemonadeChange(self, bills):
        dict_money = dict(five=0, ten=0, twenty=0)

        for bill in bills: 
            if bill == 5:
                dict_money["five"] += 1

            elif bill == 10:
                if dict_money["five"] < 1:  
                    return False
                dict_money["five"] -= 1
                dict_money["ten"] += 1

            else:  
                if dict_money["ten"] >= 1 and dict_money["five"] >= 1:
                    dict_money["ten"] -= 1
                    dict_money["five"] -= 1
                elif dict_money["five"] >= 3:
                    dict_money["five"] -= 3
                else:
                    return False

        return True
