class Solution:
    def bulbSwitch(self, n):
        if n == 0:
            return 0

        bulbList = ["_"] + [1]*n
        self.bulbsOn = n

        # print(bulbList)

        def toggle(bulb_num):
            # print(bulb_num)
            if bulbList[bulb_num] == 1:
                bulbList[bulb_num] = 0
                self.bulbsOn -= 1
            else:
                bulbList[bulb_num] = 1
                self.bulbsOn += 1

        for round in range(2, n+1):
            k = 1

            while round*k <= n:
                toggle(round*k)
                k += 1

        return self.bulbsOn


    # Works, too slow
    def bulbSwitch_1(self, n):
        if n == 0:
            return 0

        bulbList = ["_"] + [1]*n
        self.bulbsOn = n

        # print(bulbList)

        def toggle(bulb_num):
            # print(bulb_num)
            if bulbList[bulb_num] == 1:
                bulbList[bulb_num] = 0
                self.bulbsOn -= 1
            else:
                bulbList[bulb_num] = 1
                self.bulbsOn += 1

        for round in range(2, n+1):
            k = 1

            while round*k <= n:
                toggle(round*k)
                k += 1

        return self.bulbsOn

print(Solution().bulbSwitch(2))
