'''
Run-length encoding is a compression algo.

When we pass the arr [1,1,1,2,2,2,2,2]
through the compression algo, we get:
[[1,3],[2,5]]

Given two compressed arrays:
decompress them
find their product
then compress the product
return the answer
'''

# Works, too slow
# class Solution:
#     def findRLEArray(self, encoded1, encoded2):
#         def decompressArr(arr):
#             resp = []
#
#             for chr, freq in arr:
#                 resp += [chr]*freq
#
#             return resp
#
#         def compressArr(arr):
#             resp = []
#
#             i = 0
#
#             while i < len(arr):
#                 chr = arr[i]
#                 freq = 0
#                 j = i
#
#                 while j < len(arr) and chr == arr[j]:
#                     freq += 1
#                     j += 1
#
#                 resp.append([chr, freq])
#
#                 i = j
#
#             return resp
#
#
#         decompress1 = decompressArr(encoded1)
#         decompress2 = decompressArr(encoded2)
#
#         for idx in range(len(decompress1)):
#             decompress1[idx] *= decompress2[idx]
#
#         return compressArr(decompress1)

class Solution:
    def findRLEArray(self, encoded1, encoded2):
        productRLE = []

        idx1 = 0
        idx2 = 0

        while idx1 < len(encoded1) and idx2 < len(encoded2):
            chr1, freq1 = encoded1[idx1]
            chr2, freq2 = encoded2[idx2]

            product = chr1*chr2
            freq = min(freq1, freq2)

            encoded1[idx1][1] -= freq
            encoded2[idx2][1] -= freq

            if freq1 == 0:
                idx1 += 1

            if freq2 == 0:
                idx2 += 1

            if not productRLE or productRLE[-1][0] != product:
                productRLE.append([product, freq])
            else:
                productRLE[-1][1] += freq

        return productRLE





print(Solution().findRLEArray([[1,3],[2,3]], [[6,3],[3,3]]))
print(Solution().findRLEArray([[1,3],[2,1],[3,2]], [[2,3],[3,3]]))
print(Solution().findRLEArray())
