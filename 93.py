'''
A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.


So the question is whether or not we can place a period here or not.

For each subgroup, you cannot have leading zeroes, and the number that
each subgroup represents is in [0,255].
'''

class Solution:
    def restoreIpAddresses(self, s):
        address_set = set()
        n = len(s)

        def valid_group(group):
            int_rep = int(group)

            if int_rep > 255:
                return False

            if int_rep > 0 and group[0] != '0':
                return True

            if len(group) == 1:
                return True

            return False

        def backtrack(idx, address, dots):
            # print(address)
            if idx >= n-1 and dots == 0 and len(address) == n+3:
                address_set.add(address)

            if dots == 0:
                return

            for rhs in range(idx+1, min(idx+4, n+1)):
                if valid_group(s[idx:rhs]):
                    if len(address) == 0:
                        backtrack(rhs, s[idx:rhs], dots-1)
                    else:
                        backtrack(rhs, address+"."+s[idx:rhs], dots-1)

        backtrack(0, "", 4)

        return list(address_set)


print(Solution().restoreIpAddresses("25525511135"))
# print(Solution().restoreIpAddresses("00000"))
