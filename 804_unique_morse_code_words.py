'''
Ok so we are given the mapping from morse code
to character in the alphabet.

Given a list of words, return the number of different
transformations we have.

I'm not really sure what this means.

For each word, we transform to morse. Store the morse.
Check the number of unique morse strings?

I think that is correct. Ok.

For each word:
    build the morse representation.
    - for each character, get the index in our arr[str]
    - get ord and then - 93? (ord("a")-93 == 0?)
    - Keep a dict to keep track of whether or not something
      is unique.
    - also a counter, we will be returning the counter.
    - if morse is unique, add to dict, += 1 counter.

Ok so test cases:
Put in words of different length
Put in zero words
Put in words with all different morse
Put in words with all same morse

Got it right.

'''

class Solution:
    def uniqueMorseRepresentations(self, words):
        ans = 0

        charToMorse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        seen = {}

        for word in words:
            morse = ""
            for chr in word:
                morse += charToMorse[ord(chr)-97]

            if morse not in seen:
                seen[morse] = True
                ans += 1

        return ans
