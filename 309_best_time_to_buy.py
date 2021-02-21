class Solution:
    def maxProfit(self, prices):
        ...

'''
We come to a stock, we have the option of buying, selling or free.
I'll be calling them have, cool, free

So we have three states. Out of these three states only two can be
considered for an end state. Those states being: selling, cooldown.

Every time we see a new stock value, we have the opportunity to
change from one of three states. While we are in each state, we have
a certain profit, or balance. It makes sense that we should only go
from one state to another if this transition results in a higher
balance.

1) How each state should be initialized:
sell     = -inf | We don't have anything to sell
coolDown = -inf | We haven't sold anything
buy      =    0

2) State Transitions:
What does it mean to buy a stock?
it means to take a hit to your current balance.
So current_balance - stock_price.

When can we buy a stock?
We can buy a stock after we have cooled down.

We have finished cooling down when we are in a free state.

So the balance of have is the max between the current value
of max and the balance of free - the stock price we are buying
at.

This would only ever work if we previously decided to buy and sell,
made money, and now are buying again.

have = max(have, free-p)

cool is a state that we enter into after we have sold a stock.
Since have represents the state when we have the stock, a transition
from have --> cool would result in:

cool = have + stock_we_sell_at

We want to maximize, so we only do this if the result is greater.

We sell the stock every chance we get and see if that results in a max

Finally we have cool to free. After one iteration, cool becomes free.
Since we are maximizing a certain balance we have a max function.

free = max(free, cool)

if cool was updated last iteration, it is now eligible to transition this
iteration.

have = max(have, free - p)
cool = cool, have + p
free = max(free, cool )

Wrap these in one line so nothing is updated.
Start at -inf for cool, have, since we initially
need to take a loss.
'''

class Solution:
    def maxProfit(self, prices):
        free = 0
        cool = float('-inf')
        have = float('-inf')

        for p in prices:
            have, cool, free = max(have, free - p), have + p, max(free, cool)

        return max(cool, free)
