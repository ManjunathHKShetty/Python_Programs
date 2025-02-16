class Solution:
    def reverseString(self, s):
        n = len(s)
        l = 0
        r = n - 1

        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

X = Solution()
s_list = ["h","e","l","l","o"]
s_list2 = ["H","a","n","n","a","h"]
X.reverseString(s_list)
print(s_list2)
X.reverseString(s_list2)
print(s_list2)
