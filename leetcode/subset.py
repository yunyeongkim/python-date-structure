from typing import List


class Solution:
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     result = []
        
    #     def backtrack(start:int , current_subset : List[int]):
    #         result.append(current_subset.copy)

    #         for i in range(start , len(nums)):
    #             current_subset.append(nums[i])
    #             backtrack(i+1 , current_subset)
    #             current_subset.pop


    #     backtrack(0,[])
    #     return result


    def subsets(self, num: List[int]) -> List[List[int]]:
        result = []
        def backtrack (start : int , current_subset : List[int]):
            result.append(current_subset.copy())
            for i in range(start ,len(num)):
                current_subset.append(num[i])
                backtrack(i+1 , current_subset)
                current_subset.pop()

        backtrack(0,[])
        return result

sol = Solution()
print(sol.subsets([1, 2, 3]))