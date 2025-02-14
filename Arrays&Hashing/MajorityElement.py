from collections import defaultdict

class Solution:
    def majorityElement(self, nums):
        count = defaultdict(int) #(or) {}
        res, maxCount = 0, 0
        for n in nums:
            count[n] += 1       #(or) Count.get(n,0) + 1
            if maxCount < count[n]:
                res = n
                maxCount = count[n]
        return res


X = Solution()
print(X.majorityElement([2,2,1,1,1,2,2]))
print(X.majorityElement([3,2,3]))