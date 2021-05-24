'''
ruleKey == "type" and ruleValue == typei.
ruleKey == "color" and ruleValue == colori.
ruleKey == "name" and ruleValue == namei
items[i] = [typei, colori, namei]
'''

class Solution:
    def countMatches(self, items, ruleKey, ruleValue):
        ans = 0
        idx = 0
        if ruleKey == "color":
            idx = 1
        elif ruleKey == "name":
            idx = 2

        for item in items:
            if item[idx] == ruleValue: ans += 1

        return ans
