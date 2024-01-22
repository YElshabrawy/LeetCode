class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = n * (n+1) // 2
        miss = s - sum(set(nums))
        dup = sum(nums) + miss - s
        return [dup, miss]


        
[
