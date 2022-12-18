'''
Proceed from right to left
have counter start at 1, += 1 for every move,
when > 3, set to zero.

if counter == 0:
    check left 1, if in bounds and left == '1':
        continue

    append the one's place kv to the resp[string]

if counter == 1:
    append the ten's place kv to the resp

if counter == 2:
    append the one's place kv to the resp with the hundreds kv

In all cases, if the idx == 0, append the hundreds kv

If for the last two, they were both zeros, add hundred.


[11, 19] | Special case
[10, 20, 30], have 0 --> '', so nothing is included

9 876 543 210
2,147,483,648


billion
million
thousand

Problems for later:
- How to handle adding the hundreds descriptor to the front of the str
'''

from collections import deque

class Solution:
    def numberToWords(self, num):
        one_digit = {
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine'
        }

        two_digit = {
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen'
        }

        tens = {
            2: 'Twenty',
            3: 'Thirty',
            4: 'Forty',
            5: 'Fifty',
            6: 'Sixty',
            7: 'Seventy',
            8: 'Eighty',
            9: 'Ninety'
        }

        if (num == 0): return "Zero"

        def get_three_digit_num(num):
            if ( not num ) : return ""
            if ( not num// 100): return get_two_digit_num(num)
            return one_digit[ num // 100 ] + " Hundred" + ((" " + get_two_digit_num( num % 100)) if( num % 100) else "")

        def get_two_digit_num(num):
            if not num:
                return ''
            elif num < 10:
                return one_digit[num]
            elif num < 20:
                return two_digit[num]

            return tens[num//10] + ((" " + one_digit[num % 10]) if( num % 10) else "")

        billion = num // 1000000000
        million = (num - billion * 1000000000) // 1000000
        thousand = (num - billion * 1000000000 - million * 1000000) // 1000
        last_three = num - billion * 1000000000 - million * 1000000 - thousand * 1000

        result = ''
        if billion:
            result = get_three_digit_num(billion) + ' Billion'
        if million:
            if result: result += ' '
            result += get_three_digit_num(million) + ' Million'
        if thousand:
            if result: result += ' '
            result += get_three_digit_num(thousand) + ' Thousand'
        if last_three:
            if result: result += ' '
            result += get_three_digit_num(last_three)
        return result

print(Solution().numberToWords(1234567))
