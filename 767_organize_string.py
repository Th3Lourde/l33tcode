'''
Can you organize a string s.t. for all elements in list,
a[i] != a[i+1] && a[i-1] != a[i]

If sum(frequency of all characters) + 2 <= most popular character frequency, no
If sum(frequency of all characters) + 2 > most popular character frequency, no

So the data structure that I was looking for was a heap. Heaps return the largest
top 2 letters with the largest remaining counts

'''


class Solution:

    def reorganizeString(self, S):
        pq = [(-S.count(x), x) for x in set(S)]
        print(pq)

        heapq.heapify(pq)

    # def reorganizeString(self, S: str) -> str:
    def reorganizeString_1(self, S):
        if S == "":
            return ""

        freq = {}
        maxF = S[0]


        for i in range(len(S)):
            try:
                freq[S[i]] += 1

            except:
                freq[S[i]] = 1


            if freq[maxF] < freq[S[i]]:
                maxF = S[i]


        tmp = 0
        for key in freq:
            if key != maxF:
                tmp += freq[key]

        if tmp + 1 < freq[maxF]:
            return ''

        # Construct example string

        import operator

        print(freq)
        freq = sorted(freq.items(), key=operator.itemgetter(1), reverse=True)
        freq = dict(freq)
        print(freq)

        keys = list(freq.keys())

        if len(keys) == 1:
            if freq[keys[0]] == 1:
                return keys[0]
            elif freq[keys[0]] > 1:
                return ""

        if keys[0] == maxF:
            i = 1
            a = maxF
            b = keys[i]

        elif keys[0] != maxF:
            i = 0
            a = maxF

        ans = ""
        odd = True

        while i < len(keys):
            b = keys[i]

            if odd:
                ans += (str(a)+str(b))*min(freq[a], freq[b])

            elif not odd:
                ans += (str(b)+str(a))*min(freq[a], freq[b])

            if freq[a] > freq[b]:
                freq[a] -= freq[b]
                freq[b] = 0

            elif freq[a] < freq[b]:
                freq[b] -= freq[a]
                freq[a] = 0
                a = b
                odd = not odd

            elif freq[a] == freq[b]:
                freq[a],freq[b] = 0,0

                if i+1 < len(keys):
                    a = keys[i+1]
                    i += 1

                elif i+1 >= len(keys):
                    break

            i += 1

        print("a: {}, freq[a]: {}, b: {}, freq[b]: {}".format(a, freq[a], b, freq[b]))

        if freq[a] > 0:
            if ans[0] == a:
                ans += a

            elif ans[0] != a:
                ans = str(a) + ans

            freq[a] -= 1

        while freq[a] > 0:
            j = 2
            for i in range(freq[a]):
                ans = ans[:j] + a + ans[j:]
                j += 2
                freq[a] -= 1

        return ans



if __name__ == '__main__':
    s = Solution()
    # print(s.reorganizeString("aab"))

    # a = "gpneqthatplqrofqgwwfmhzxjddhyupnluzkkysofgqawjyrwhfgdpkhiqgkpupgdeonipvptkfqluytogoljiaexrnxckeofqojltdjuujcnjdjohqbrzzzznymyrbbcjjmacdqyhpwtcmmlpjbqictcvjgswqyqcjcribfmyajsodsqicwallszoqkxjsoskxxstdeavavnqnrjelsxxlermaxmlgqaaeuvneovumneazaegtlztlxhihpqbajjwjujyorhldxxbdocklrklgvnoubegjrfrscigsemporrjkiyncugkksedfpuiqzbmwdaagqlxivxawccavcrtelscbewrqaxvhknxpyzdzjuhvoizxkcxuxllbkyyygtqdngpffvdvtivnbnlsurzroxyxcevsojbhjhujqxenhlvlgzcsibcxwomfpyevumljanfpjpyhsqxxnaewknpnuhpeffdvtyjqvvyzjeoctivqwann"


    # print(s.reorganizeString(a))

    a = "qhehehehehehehehehehehehehehehehehehehehehehehehehehehehemcmcmcmcmcmcmcmcmcmcmcmcmcmcmcmcmcmcmcmcmcmcmcmcmcmcnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvfvfyfyfyfyfyfyfyfyfyfyfyfyfyfyfyfyfyfyfyfyfyayawawawawawawawawawawawawawawawawawawawawawkukukukukukukukukukukukukukukukukukukukuksrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrspxpxpxpxpxpxpxpxpxpxpxpxpxpxpxpxpxpxgogogogogogogogogogogogogogogogogobtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtdididididididididididididididizizlzlzlzlzlzlzlzlzlzlzlzjzjqjqjqjqjqjqjqjqjqj"

    print(s.reorganizeString(a))
