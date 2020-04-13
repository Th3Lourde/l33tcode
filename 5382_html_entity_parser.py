


def entityParser(text):
    d = {
        "&quot;":'"',
        "&apos;":"'",
        "&amp;": "&",
        "&gt;": ">",
        "&lt;": "<",
        "&frasl;":"/",
    }

    s = 0
    e = 0

    ans = ""

    while s <= len(text)-4:
        if text[s] == "&":
            e = s
            while e < len(text) and text[e] != ";":
                e +=1

            try:
                if d[text[s:e+1]]:
                    nwStr = d[text[s:e+1]]
                    ans += nwStr
                    s = e+1
            except:
                ans += "&"
                s += 1

        elif text[s] != "&":
            ans += text[s]
            s += 1


    return ans + text[s:]


# tc = ["&amp; is an HTML entity but &ambassador; is not."]


testCases = [
    ["&amp; is an HTML entity but &ambassador; is not.", "& is an HTML entity but &ambassador; is not."],
    ["and I quote: &quot;...&quot;", "and I quote: \"...\""],
    ["Stay home! Practice on Leetcode :)", "Stay home! Practice on Leetcode :)"],
    ["x &gt; y &amp;&amp; x &lt; y is always false", "x > y && x < y is always false"],

]

passed = True
z = 1

for testCase in testCases:
    resp = entityParser(testCase[0])

    if resp != testCase[1]:
        passed = False
        print("[failed test case {}]  {}  |||  {}".format(z, testCase[1], resp))
        break

    z += 1

if passed:
    print("[passed all test cases] :)")
