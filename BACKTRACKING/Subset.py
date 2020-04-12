class Solution:

    def subset(self, s):
        res = self.subset_helper([], sorted(s))
        res.sort()
        return res

    def subset_helper(self, curr, s):
        print([curr]) ##
        if s:
            return self.subset_helper(curr, s[1:])+self.subset_helper(curr + [s[0]], s[1:])
        return [curr]


c = Solution()

s = [1, 2, 3]

print(c.subset(s))
