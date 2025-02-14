class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        min_len = min(len(s) for s in strs)
        if min_len == 0:
            return ""
        for i in range(min_len):
            current_char = strs[0][i]
            for s in strs[1:]:
                if s[i] != current_char:
                    return strs[0][:i]
        return strs[0][:min_len]

X = Solution()
print(X.longestCommonPrefix(["flower","flow","flight"]))
print(X.longestCommonPrefix(["dog","racecar","car"]))