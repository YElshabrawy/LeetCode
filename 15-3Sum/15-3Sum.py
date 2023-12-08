        output = []
        nums.sort()
        for num, i in enumerate(nums):
            j = num + 1
            k = len(nums) - 1
            if num > 0 and i == nums[num - 1]:
                continue
            while j < k:
                sum=i+nums[j]+nums[k]
                if sum==0:
                    output.append([i,nums[j],nums[k]])
                    j+=1
                    while nums[j]==nums[j-1] and j<k:
                        j+=1
                elif sum<0:  
                    j+=1
                else:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
class Solution:
[
