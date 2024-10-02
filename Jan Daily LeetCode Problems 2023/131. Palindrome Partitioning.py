class Solution:

    def partition(self, s):

        if len(s) == 0:
            return []

        ans = []

        for i in range(1, len(s) + 1):

            if s[:i] == s[:i][::-1]:
                for remainigChar in self.partition(s[i:]):
                    ans.append([s[:i]] + remainigChar)
        return ans