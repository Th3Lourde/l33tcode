'''
Given a list of products,
return the three products
that are most similar with searchWord.

Do a search for every character in searchWord.

So return a list of lists. len(ans) == len(searchWord).

Sort the given list by lexi order.

We are just changing the first index, then returning
the next three words (assuming we have room).

.sort() works good.

next we need to find the next index.
We can directly compare strings, dope.

We can just do a search. Find the element
that is closest to our search.

We care about maximizing the number of elements that
are held in common, then compare distance of element
furthest on the end.

Only do the compare if we have the same number of shared elements.

do a search and find the max

When we find something that is less than the max, done.

# maxW = [index, nums_similar, word]
maxW = [nums_similar, index, word]

maxW = None

Compute number of shared elements, compare to maxW.

Ok so I could have totally done a better job, however
good on me for deciding to do the binary search.

I think that this was a learning experience w.r.t.
lexicographical sort. I was struggling to solve that
problem yet didn't actually need to solve it.

Ok so maybe everything has to match search word

Ok I finally got it. Jesus. Time complexity was very good
though. Props for me.

'''
class Solution:
    def suggestedProducts(self, products, searchWord):
        def findClosest(products, searchWord):

            # If searchWord == "", do what?


            lo = 0
            hi = len(products)-1
            mid = None

            while lo < hi:
                mid = lo + int((hi-lo)/2)

                if products[mid][0] == searchWord[0]:
                    break

                elif products[mid][0] > searchWord[0]:
                    hi = mid - 1

                elif products[mid][0] < searchWord[0]:
                    lo = mid + 1

            if products[0][0] == searchWord[0]:
                mid = 0

            if mid == None or products[mid][0] != searchWord[0]:
                # print("No Match")
                return -1, []

            while mid >= 0 and products[mid][0] == searchWord[0]:
                mid -= 1

            mid += 1

            while searchWord > products[mid]:
                mid += 1

            resp = []

            for i in range(0, 3):
                if mid+i < len(products) and searchWord == products[mid+i][:len(searchWord)]:
                    resp.append(products[mid+i])

                else:
                    break

            return mid, resp


        products.sort() # Sorts the words in lexicographical order

        ans = []

        for i in range(1, len(searchWord)+1):
            index, tmp = findClosest(products, searchWord[:i])
            ans.append(tmp)

            if index >= 0:
                products = products[index:]


        return ans
'''
This doesn't mean we have found the best match.
We would have to back track until we find it.
Binary search, backtract until not true.

given 'mon', and 'monk' and 'monz' <-- keep 'monk'?

Do I even need to check this, or does lexicographical
sort actually take care of this? I think it does.

So once we have maximized shared, we are done.

if two elements have the same shared, if current < next,
keep current?

So the first time the comparison is False, that is our index.

'''
# def closer(maxV, shared, searchWord):
#     if maxV[0] == len(searchWord):
#         # compare last element
#
#
#     elif maxV[0] != len(searchWord):
#         # start from maxV[0]-1 and compare
#         # to see which character is closer

# Geez this was hot trash
'''
Ok so this returns the index of the closest
element. Let's have this return the query of
each word.
'''

# findClosest(["mobile","mouse","moneypot","monitor","mousepad"], "mouse")

# findClosest(["abc", "mobile","mouse", "helloworld","moneypot","monitor","mousepad"], "hell")

if __name__ == '__main__':
    s = Solution()

    print(s.suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], "mouse"))

    print(s.suggestedProducts(["bags","baggage","banner","box","cloths"], "bags"))

    print(s.suggestedProducts(["havana"], "havana"))

    print(s.suggestedProducts(["havana"], "tatiana"))
