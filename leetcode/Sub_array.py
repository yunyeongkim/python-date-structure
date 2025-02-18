class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        def __sub_function(i , current_sum, max_sum):
            if i == len(nums):
                return max_sum

            current_sum += nums[i]
            max_sum= max(max_sum, current_sum)
            print(f"i= {i} ,current ={current_sum} , max ={max_sum}")

            if current_sum < 0 :
                current_sum = 0
            return __sub_function(i+1,current_sum,max_sum)
        
        return __sub_function(0,0,nums[0])
    
    def maxSubArray_sol(self, nums: list[int]) -> int:            
        res = nums[0]  # 최댓값 저장 (초기값: 첫 번째 요소)
        total = 0  # 현재까지의 합

        for n in nums:
            if total < 0:
                total = 0  # 음수라면 리셋 (새로운 부분 배열 시작)
            print(f"total = {total}")
            total += n  # 현재 숫자를 더함
            res = max(res, total)  # 최댓값 갱신
            print(f"total = {total} , res = {res}")
        
        return res
    

sol = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(sol.maxSubArray_sol(nums))