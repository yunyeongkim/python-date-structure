'''
Given an integer array nums, 
return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
'''
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()  # 1️⃣ 정렬
        result = []

        for i in range(len(nums) - 2): 
            if i > 0 and nums[i] == nums[i - 1]:  
                continue
            j, k = i + 1, len(nums) - 1  
            while j < k:  
                num_sum = nums[i] + nums[j] + nums[k]
                if num_sum == 0: 
                    result.append([nums[i], nums[j], nums[k]])

                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif num_sum < 0:
                    j += 1 
                else:
                    k -= 1 
        return result



sol = Solution()
nums = [-1,0,1,2,-1,-4]
print(sol.threeSum(nums))

        