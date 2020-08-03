'''
Ok so we are reversing the algo

Algo:
    - Take the top off of the deck
    - If card.next() == True, put next card at the bottom

Reverse Algo:
Start at sorted array

[17,13,11,2,3,5,7]

[2,3,5,7,11,13,17]
   ^         ^

[2,13,5,7,11,3,17]
   ^         ^

[2,13,5,7,11,3,17]
      ^      ^

[2,13,3,7,11,5,17]
      ^      ^

[2,13,3,7,11,5,17]
        ^    ^

[2,13,3,5,11,7,17]
        ^    ^



[2,3,5,7,11,13,17]

[17]

[13, 17]

So just reverse the algo. Fml.

Have the sorted list,

ans = []

while sorted list is not empty:
    ans = sorted.pop() + ans

    tmp = ans.pop()
    ans = tmp + ans



[2,3,5,7,11,13,17]

ans = [17]
switch: [17]

[2,3,5,7,11,13]

ans = [13,17] → [17, 13]

[2,3,5,7,11]

ans = [11, 17, 13] → [13, 11, 17]


[2,3,5,7]

ans = [7, 13, 11, 17] → [17, 7, 13, 11]


[2,3,5]
[17, 7, 13, 11]

[2,3,5]
[17, 7, 13, 11]

[2,3]
[5, 17, 7, 13, 11] → [11, 5, 17, 7, 13]

[2]
[3, 11, 5, 17, 7, 13] → [13, 3, 11, 5, 17, 7]

[2]
[13, 3, 11, 5, 17, 7]

[2, 13, 3, 11, 5, 17, 7]

[2, 13, 3, 11, 5, 17, 7] # So only switch if we have an element left in the list.


inp : [2,3,5,7,11,13,17]
goal: [2,13,3,11,5,17,7]

'''

class Solution:
    def deckRevealedIncreasing(self, deck):
        deck.sort()

        ans = []

        while deck:
            tmp = deck.pop()
            ans = [tmp] + ans

            if deck:
                ans = [ans[-1]] + ans
                ans.pop()

        return ans




if __name__ == '__main__':
    s = Solution()

    print(s.deckRevealedIncreasing([17,13,11,2,3,5,7]))
