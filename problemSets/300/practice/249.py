class Solution:
    def groupStrings(self, strings):
        d = {}
        for s in strings:
            key = ()
            for idx in range(len(s)-1):
                diff = 26 + ord(s[idx+1]) - ord(s[idx])
                key += (diff%26,)

            if key in d:
                d[key].append(s)
            else:
                d[key] = [s]

        return list(d.values())

    # def groupStrings(self, strings: List[str]) -> List[List[str]]:
    # 	hashmap = {}
    # 	for s in strings:
    # 		key = ()
    # 		for i in range(len(s) - 1):
    # 			circular_difference = 26 + ord(s[i+1]) - ord(s[i])
    # 			key += (circular_difference % 26,)
    # 		hashmap[key] = hashmap.get(key, []) + [s]
    # 	return list(hashmap.values()


print(Solution().groupStrings(["abc","bcd","acef","xyz","az","ba","a","z"]))
print(Solution().groupStrings(["a","a","b","b","c","c"]))
print(Solution().groupStrings(["a","b","c","a","b","c"]))



[["fpbnsbrkbcyzdmmmoisaa"],["cpjtwqcdwbldwwrryuclcngw"],["a","l","i","d"],["fnuqwejouqzrif"],["js"],["qcpr"],["zghmdiaqmfelr","yfglchzpledkq"],["iedda"],["dgwlvcyubde","ilbqahdzgij"],["lpt"],["qzq","sbs"],["zkddvitlk"],["xbogegswmad"],["mkndeyrh"],["llofdjckor","kknecibjnq"],["lebzshcb","ohecvkfe"],["firomjjlidqpsdeqyn"],["dclpiqbypjpfafukqmjnjg","yxgkdlwtkekavapflheieb"],["lbpabjpcmkyivbtgdwhzlxa"],["wmalmuanxvjtgmerohskwil"],["oraxvssurmzybmnzhw"],["wuxnoibr"],["gkxpnpbfvjm"],["lwpphufxw"],["txb"],["zvuur"],["eqdf"],["nw"],["aiplrzejplumda"],["huoybvhibgqibbwwdzhqhslb"],["rbnzendwnoklpyyyauemm"]]

[["eqdf","qcpr"],["lpt","txb"],["yfglchzpledkq","zghmdiaqmfelr"],["kknecibjnq","llofdjckor"],["cpjtwqcdwbldwwrryuclcngw","huoybvhibgqibbwwdzhqhslb"],["lbpabjpcmkyivbtgdwhzlxa","wmalmuanxvjtgmerohskwil"],["iedda","zvuur"],["js","nw"],["lebzshcb","ohecvkfe"],["dgwlvcyubde","ilbqahdzgij"],["lwpphufxw","zkddvitlk"],["qzq","sbs"],["dclpiqbypjpfafukqmjnjg","yxgkdlwtkekavapflheieb"],["mkndeyrh","wuxnoibr"],["firomjjlidqpsdeqyn","oraxvssurmzybmnzhw"],["gkxpnpbfvjm","xbogegswmad"],["fpbnsbrkbcyzdmmmoisaa","rbnzendwnoklpyyyauemm"],["aiplrzejplumda","fnuqwejouqzrif"]]


["eqdf","qcpr"]
["lpt","txb"]
["cpjtwqcdwbldwwrryuclcngw","huoybvhibgqibbwwdzhqhslb"]
