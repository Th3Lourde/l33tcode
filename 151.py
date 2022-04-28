
from collections import deque

class Solution:
    def reverseWords(self, s):
        list = s.split(" ")
        list_of_words = []

        for word in list:
            if len(word) == 0:
                continue

            list_of_words.append(word)

        # print(list_of_words)

        reversed_words = list_of_words[::-1]

        return " ".join(reversed_words)


print(Solution().reverseWords("  Bob    Loves  Alice   "))
