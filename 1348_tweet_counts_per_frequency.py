

'''
Implement a class that has two methods:

1) recordTweet(str, int)
store the tweetName at the recorded time
time is always given in seconds

2) getTweetCountsPerFrequency(string freq, string name, int start, int end)
return the number times a tweet matching tweet name was tweeted.
freq can be [second, minute, hour]

Ok so there are two things that we need to come up with:
how to store the data
how to query the data

Very similar topics. Anyways:

How about we use a dict as our database.

the key is the tweet, the value is the time(s) when
the tweet was made.

when searching, we do a conversion to seconds
then find number of tweets in the given time boundaries.

It is important that we keep our db sorted, or else the reads
will suffer greatly.

Ok so how do we store?

If there is already something there, perform binary search.
If the term <= our term, just insert it there.

Else insert left of term that we get.

[0,0,0,0,0]
 l       r

I'm too tired for this, just append it and sort after append

Again, read the problem. Mis-interpretted frequency. Oh well,
time for bed.

Ok so we want to create a sliding window and count the number
of elements in that window.

This sounds kinda like a prefix tree?

We have a left pointer and a right pointer.
We keep incrementing the pointers. The pointers land on elements
that are within the given range.

If our left pointer doesn't find anything valid, we call it quits

So the first step is to calibrate our left pointer, then to calibrate
our right pointer.

We should also remember where our previous left pointer was, or where
our previous right pointer was

We can call this variable starting.

Initially starting is zero, then we set it equal to last

Determine bounds on iteration

We could also pre-compile our intervals using the lowest, highest values

[0, 40] seconds

start = [0]
delta = [1]-[0]

maxTime = [-1]

if start > maxTime:
    break


.append([start, start*delta])

start = start*delta
delta*= 2





400



3

starting = -1
l = starting+1
rGoal = 3

[1,2,3,6,7,8,10]
 l

starting =  -1
lGoal = startTime
rGoal = endTime
results = 0

l = starting


while arr[l] < lGoal:
    l += 1

r = l

while arr[r] <= rGoal:
    r += 1
    ans += 1





'''


class TweetCounts:

    def __init__(self):
        self.db = {}

    def recordTweet(self, tweetName, time):
        if tweetName not in self.db:
            self.db[tweetName] = [time]

        elif tweetName in self.db:
            idx = len(self.db[tweetName])

            for i in range(len(self.db[tweetName])):
                if self.db[tweetName][i] >= time:
                    idx = i
                    break


            self.db[tweetName].insert(idx, time)

        # Are startTime, endTime times in seconds?
    def getTweetCountsPerFrequency(self, freq, tweetName, startTime, endTime):

        delta = 1

        if freq == "minute":
            # startTime *= 60
            # endTime *= 60
            delta *= 60

        elif freq == "hour":
            # startTime *= 60*60
            # endTime *= 60*60
            delta *= 60*60

        elif freq == "day":
            # startTime *= 60*60*12
            # endTime *= 60*60*12
            delta *= 60*60*12

        if tweetName not in self.db:
            # Would we instead want a list of zeroes.
            return 0

        # delta -= 1


        # Max val:
        maxTime = self.db[tweetName][-1]

        if startTime > maxTime:
            return [0]

        start = startTime
        ans = []


        # Tweets
        tweets = self.db[tweetName]

        idx = 0

        while start > tweets[idx]:
            idx += 1

        # print(endTime)

        while start <= maxTime and start <= endTime:
            # print(start)
            tmp = 0

            while tweets[idx] <= endTime and start <= tweets[idx] < start+delta:

                tmp += 1

                if tweets[idx] == maxTime:
                    break

                idx += 1

            ans.append(tmp)
            start += delta

        while start <= endTime:
            ans.append(0)

            start += delta

        # Remove trailing zeroes

        return ans

if __name__ == '__main__':
    tc = TweetCounts()

    tc.recordTweet("tweet3", 0);
    tc.recordTweet("tweet3", 60);
    tc.recordTweet("tweet3", 10);

    # tc.recordTweet("hello", 123)
    # tc.recordTweet("hello", 3)
    # tc.recordTweet("hello", 234)

    tc.db

    tc.getTweetCountsPerFrequency("minute", "tweet3", 0, 59)
    tc.getTweetCountsPerFrequency("minute", "tweet3", 0, 60)

    tc.recordTweet("tweet3", 120)

    tc.getTweetCountsPerFrequency("hour", "tweet3", 0, 210)

    # tc.getTweetCountsPerFrequency("seconds", "hello", 200, 1000)
