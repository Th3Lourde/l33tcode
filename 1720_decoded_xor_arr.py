class Solution:
    def decode(self, encoded, first):
        decoded = [first]
        i = 0

        while i < len(encoded):
            decoded.append(decoded[i]^encoded[i])
            i += 1

        return decoded

if __name__ == '__main__':
    s = Solution()
    print(s.decode([1,2,3], 1))
    print(s.decode([6,2,7,3], 4))
