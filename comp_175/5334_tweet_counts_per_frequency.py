


class TweetCounts:
    def __init__(self):
        # key = tweet, val: time
        self.data = {}

    def recordTweet(self, tweetName, time):
        try:
            self.data[tweetName].append(time)
        except:
            self.data[tweetName] = [time]

    def getTweetCountsPerFrequency(self, freq, tweetName, startTime, endTime):

        try:
            data = self.data[tweetName]

        except:
            return [0]

        if data == []:
            return [0]

        if freq == 'second':
            time_mult = 1
        elif freq == 'minute':
            time_mult = 60
        elif freq == 'hour':
            time_mult = 60*60

        data.sort()

        ans = []
        lastFind = 0
        tmp = 0

        intervalNum = 1
        i = 0

        # Search for 0 --> time_mult
        # then for time_mult --> time_mult*2
        # ... You run out of elements
        lbound = time_mult*(intervalNum-1)
        rbound = time_mult*(intervalNum)-1

        while i <= len(data)-1 and data[i] <= endTime:

            if (data[i] >= lbound and data[i] <= rbound) and (data[i] >= startTime and data[i] <= endTime):
                tmp += 1

            elif data[i] > rbound:
                ans.append(tmp)
                tmp = 1
                intervalNum += 1
                lbound = time_mult*(intervalNum-1)
                rbound = time_mult*(intervalNum)-1

            i += 1

        ans.append(tmp)
        return ans

        # for d in data:
        #     if (d >= startTime and d <= endTime):
        #
        #         if d-lastFind <= time_mult:
        #             tmp += 1
        #
        #         elif d-lastFind > time_mult:
        #             ans.append(tmp)
        #             tmp = 1
        #             lastFind = d
        #
        #
        #         # lastFind = d
        #         # ans +=1
        #
        # print(ans)
        # return [ans]



if __name__ == '__main__':
    tweetCounts = TweetCounts()

    tweetCounts.recordTweet("tweet3", 0)
    tweetCounts.recordTweet("tweet3", 60)
    tweetCounts.recordTweet("tweet3", 10)
    print(tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 59))
    print(tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 60))
    tweetCounts.recordTweet("tweet3", 120)
    print(tweetCounts.getTweetCountsPerFrequency("hour", "tweet3", 0, 210))
