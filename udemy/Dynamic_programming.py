
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        pointer = 0
        while pointer < len(nums):
            for i in range(pointer+1,len(nums)):
                if nums[pointer] + nums[i] == target:
                    return [pointer, i]
            pointer += 1
        return []
    
    def twoSum_second(self, nums: list[int], target: int) -> list[int]:
        num_map = {}
        for i , num in enumerate(nums):
            diff = target - num
            if diff in num_map:
                return [num_map[diff],i]
            num_map[num] = i 
        return []


solution = Solution()
nums = [2,7,11,15]
target = 22
print(solution.twoSum_second(nums, target))
