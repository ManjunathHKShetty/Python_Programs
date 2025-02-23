class Solution:
    def validPalindrome(self, s):
        n = len(s)
        l = 0
        r = n - 1

        while l < r:
            if s[l] != s[r]:
                skipL = s[l+1:r+1]
                skipR = s[l:r]
                return (skipL == skipL[::-1] or skipR == skipR[::-1])

            l += 1
            r -= 1

        return True

X = Solution()
result_1 = X.validPalindrome("abca")
print(result_1)
result_2 = X.validPalindrome("abc")
print(result_2)