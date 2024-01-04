class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums = sorted(nums)

        def backtrack(start, curr):
            output.append(curr)
            for i in range(start, len(nums)):
                backtrack(i + 1, curr + [nums[i]])

        backtrack(0, [])
        return output
[
