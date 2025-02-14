class Solution:
    #Method1
    def hasDuplicate(self, nums):
        return len(set(nums)) < len(nums)

    #Method2
    def hasDuplicate1(self, nums):
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False

X = Solution()
print(X.hasDuplicate([1,2,3,1]))
print(X.hasDuplicate1([1,2,3,4]))