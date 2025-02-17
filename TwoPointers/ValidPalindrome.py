class Solution:
    def validPalindrome(self, s):
        n = len(s)
        l = 0
        r = n - 1

        while l < r:
            if not s[l].isalnum():
                l += 1
                continue

            if not s[r].isalnum():
                r -= 1
                continue

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True

X = Solution()
result_1 = X.validPalindrome("ra_ c_e_ CAR")
print(result_1)
result_2 = X.validPalindrome("tab a cat")
print(result_2)