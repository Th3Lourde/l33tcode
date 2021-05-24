'''
Given string num (large integer) and integer k.

Call an integer wonderful if it is a permutation
of the digits in num and is greater in value than
num.

Return the minimum number of adjacent digit swaps
that needs to be applied to num to reach the kth
smallest wonderful integer.

So get the next biggest number k times and return
the number of swaps required

Find the highest index i such that s[i] < s[i+1]
Find the highest index j > i such that s[j] > s[i].
Such a j must exist, since i+1 is such an index.
Swap s[i] with s[j].
Reverse the order of all of the elements after index i till the last element.

0 | "5489355142"
            i
             j

0 | "5489355214"

1 | "5489355214"
2 | "5489355241"
3 | "5489355412"
4 | "5489355421"

"1234"
 ^

"1423"
   ^

       private int diff(char[] target, char[] arr) {
        int result = 0;
        for (int i=0; i<target.length; i++) {
            if (target[i] != arr[i]) {
                for (int j=i+1; j<arr.length; j++) {
                    if (arr[j] == target[i]) {
                        result += j-i;
                        while (j>i) {
                            char temp = arr[j];
                            arr[j] = arr[j-1];
                            arr[j-1] = temp;
                            j--;
                        }
                        break;
                    }
                }
            }
        }
        return result;
    }
'''

class Solution:
    def getMinSwaps(self, num, k):
        def nextPermutation(s):
            # 1) Find highest index i s.t. s[i] < s[i+1]
            s = list(s)
            highestI = 0

            for i in range(len(s)-1):
                if s[i] < s[i+1]:
                    highestI = i

            # 2) Find the highest index j > i s.t. s[j] > s[i]
            highestJ = 0

            for j in range(highestI+1, len(s)):
                if s[j] > s[highestI]:
                    highestJ = j

            # Swap s[i] with s[j].
            s[highestI], s[highestJ] = s[highestJ], s[highestI]

            # Reverse the order of all of the elements
            # after index i till the last element.
            # print(s)
            tmp = s[highestI+1:]
            tmp = tmp[::-1]

            respS = s[:highestI+1] + tmp

            return ''.join(respS)

        t = num

        # 1) Find k-th wonderful #
        for _ in range(k):
            t = nextPermutation(t)

        def minimumSwap(s1, s2):
            minSwap = 0
            i = 0
            j = 0

            while i < len(s1):
                if s1[i] == s2[j]:
                    i += 1
                    j += 1
                else:
                    if i == len(s1)-1:
                        for z in range(i-1, -1, -1):
                            if s1[i] == s2[z]:
                                minSwap = max(minSwap, i-z)
                    else:
                        for z in range(i+1, len(s2)):
                            if s1[i] == s2[z]:
                                minSwap = max(minSwap, z-i)

                    i += 1
                    j += 1

            return minSwap

        return minimumSwap(num,t)

print(Solution().getMinSwaps("5489355142", 4))
