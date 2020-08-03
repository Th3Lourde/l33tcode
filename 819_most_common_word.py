
'''
Given long string,
return word that happens most often,
where the word is not in banned.

[a,b,c]

f(x) --> 0

f(b)

a =  list(int)

max_v = a[0]
max_i = 0

for i in range(1, len(a)):
    if a[i] > max_v:
        max_v = a[i]
        max_i = i


'''



class Solution:
    def mostCommonWord(self, paragraph, banned):
        banWords = set()

        for ban in banned:
            banWords.add(ban)

        punc = ["!", "?", "'", ",", ";", "."]

        paragraph = paragraph.lower()

        for p in punc:
            if p in paragraph:
                paragraph = paragraph.replace(p, "")

        werds = paragraph.split(" ")

        dict = {}

        for werd in werds:
            if werd not in banWords:
                if werd in dict:
                    dict[werd] += 1

                elif werd not in dict:
                    dict[werd] = 1

        keys = list(dict.keys())

        ans = []

        for k in keys:
            ans.append([k, dict[k]])

        ans.sort(key = lambda x: x[1], reverse=True)

        return ans[0][0]

if __name__ == '__main__':
    s = Solution()

    print(s.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["ball"]))
