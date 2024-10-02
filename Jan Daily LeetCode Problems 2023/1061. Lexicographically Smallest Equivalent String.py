class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        lookup = defaultdict(set)
        for s in string.ascii_lowercase:
            lookup[s].add(s)

        for i in range(len(s1)):
            temp = set()
            del_list = []
            for key, value in lookup.items():
                if s1[i] in value or s2[i] in value:
                    temp.update(value)
                    del_list.append(key)
            for key in del_list:
                del lookup[key]
            if temp:
                lookup[min(temp)].update(temp)

        # print(lookup)
        res = [''] * len(baseStr)
        for i in range(len(baseStr)):
            for key, value in lookup.items():
                if baseStr[i] in value:
                    res[i] = key
        return ''.join(res)