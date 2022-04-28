class Solution:
    def romanToInt(self, num):
        symbol_to_value = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
            "IV" : 4,
            "IX" : 9,
            "XL" : 40,
            "XC" : 90,
            "CD" : 400,
            "CM" : 900,
        }

        val = 0
        idx = 0

        while idx < len(num):
            if idx == len(num)-1:
                val += symbol_to_value[num[idx]]
            else:
                if num[idx:idx+2] in symbol_to_value:
                    val += symbol_to_value[num[idx:idx+2]]
                    idx += 1
                else:
                    val += symbol_to_value[num[idx:idx+1]]

            idx += 1

        return val
