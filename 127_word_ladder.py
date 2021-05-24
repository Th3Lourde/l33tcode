'''
1) Create dict from word to all words that we can get to.
2) If endWord not in wordList, return 0
3) backtracking solution. Cache strings that we started from.

beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
                               ^

d = {
    "hit" : ["hot"],
    "hot" : ["dot", "lot"],
    "dot" : ["hot", "lot"],
    "dog" : ["dot", "log", "cog"],
    "lot" : ["log", "hot", "dot"]
    ...
}

I don't know why this is wrong and it looks like we
actually picked the wrong algo.

Let's try bfs

bfs is worse

Ok. So one problem is that I don't actually
understand why my bfs, top-down fails.


'''
from collections import deque
from collections import defaultdict
class Solution:
    def ladderLength_1(self, beginWord, endWord, wordList):
        def isOneDiff(s1, s2):
            diff = 0

            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    diff += 1

            return diff <= 1

        d = {beginWord: set()}

        for w in wordList:
            d[w] = set()

        for word in wordList:
            if isOneDiff(beginWord, word):
                d[beginWord].add(word)

        # Creating d[w1] --> []
        for w1 in wordList:
            for w2 in wordList:
                if w1 == w2:
                    continue

                if isOneDiff(w1, w2):
                    d[w1].add(w2)
                    d[w2].add(w1)

        # Top-Down with caching
        memo = {}

        def topDown(currentWord, seen):
            if currentWord == endWord:
                return 0

            if currentWord in memo:
                return memo[currentWord]

            minLadderLength = float('inf')

            for word in d[currentWord]:
                if word not in seen:
                    seen.add(word)
                    minLadderLength = min(minLadderLength, topDown(word, seen)+1)
                    seen.remove(word)

            memo[currentWord] = minLadderLength

            return memo[currentWord]

        topDown(beginWord, set())

        if memo[beginWord] < float('inf'):
            return memo[beginWord]+1

        return 0

    def ladderLength_2(self, beginWord, endWord, wordList):
        def isOneDiff(s1, s2):
            diff = 0

            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    diff += 1

            return diff <= 1

        d = {beginWord: set()}

        for w in wordList:
            d[w] = set()

        for word in wordList:
            if isOneDiff(beginWord, word):
                d[beginWord].add(word)

        # Creating d[w1] --> []
        for w1 in wordList:
            for w2 in wordList:
                if w1 == w2:
                    continue

                if isOneDiff(w1, w2):
                    d[w1].add(w2)
                    d[w2].add(w1)

        # queue = [(beginWord, set({beginWord}))]
        queue = deque()
        queue.appendleft((beginWord, 1))

        seen = set({beginWord})

        # print(d)

        while queue:
            # print(queue)
            word, numWordsSeen = queue.pop()

            seen.add(word)

            if word == endWord:
                return numWordsSeen

            else:
                for nextWord in d[word]:
                    if nextWord not in seen:
                        queue.appendleft((nextWord, numWordsSeen+1))

        return 0

    def ladderLength(self, beginWord, endWord, wordList):
        alpha = "abcdefghijklmnopqrstuvwxyz"

        m = len(beginWord)
        n = len(wordList)

        wordList.append(beginWord)

        word_inverse = {w:i for i,w in enumerate(wordList)}

        print(word_inverse)

        words_graph = defaultdict(set)

        for word in wordList:
            for idx in range(m):
                l, r = word[0:idx], word[idx+1:]

                for letter in alpha:
                    tmp = l + letter + r

                    if tmp in word_inverse and tmp != word:
                        words_graph[word_inverse[word]].add(word_inverse[tmp])

        print(words_graph)

        print(word_inverse)


s = Solution()

print(s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
print(s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]))
print(s.ladderLength("cet", "ism", ["kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos","son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun","try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen","odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix","cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup","jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant","net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot","del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all","pad","hah","hie","aim","ike","jed","ego","mac","baa","min","com","ill","was","cab","ago","ina","big","ilk","gal","tap","duh","ola","ran","lab","top","gob","hot","ora","tia","kip","han","met","hut","she","sac","fed","goo","tee","ell","not","act","gil","rut","ala","ape","rig","cid","god","duo","lin","aid","gel","awl","lag","elf","liz","ref","aha","fib","oho","tho","her","nor","ace","adz","fun","ned","coo","win","tao","coy","van","man","pit","guy","foe","hid","mai","sup","jay","hob","mow","jot","are","pol","arc","lax","aft","alb","len","air","pug","pox","vow","got","meg","zoe","amp","ale","bud","gee","pin","dun","pat","ten","mob"]))
