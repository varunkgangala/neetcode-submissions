class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        nums.sort()
        current=1
        longest=1
        for i in range(1,n):
            if nums[i]==nums[i-1]+1:
                current+=1
            elif nums[i-1]==nums[i]:
                continue
            else:
                current=1
            longest=max(longest,current)
        return longest