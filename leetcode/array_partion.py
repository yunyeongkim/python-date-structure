class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        # Bubble sort.
        for i in range(len(nums) -1, 0 , -1 ):
            for j in range(i):
                if nums[j] > nums[j+1]:
                    temp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = temp

        # Sum get min
        min_sum = 0
        for i in range(0,len(nums),2):
            min_sum += nums[i]

        return min_sum
        


solution = Solution()
nums = [1,4,3,2]
print(solution.arrayPairSum(nums))
print(nums)

nums2 = [6,2,6,5,1,2]
print(solution.arrayPairSum(nums2))
print(nums2)