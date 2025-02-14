class Solution:
    #Method1
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)

    #Method2(HashTable)
    def isAnagram2(self, s, t):
        CountS, CountT = {}, {}
        for i in range(len(s)):
            CountS[s[i]] = 1 + CountS.get(s[i],0)
            CountT[t[i]] = 1 + CountS.get(t[i], 0)

        return CountS == CountT


X = Solution()
result1 = X.isAnagram("racecar","carrace")
result2 = X.isAnagram2("jar", "jam")
print(result1)
print(result2)