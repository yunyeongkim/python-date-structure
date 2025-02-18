class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []

        def __backtracker(start,path, target):

            if target == 0:
                result.append(path[:])
            for i in range(start , len(candidates)):
                num = candidates[i]

                if num > target:
                    continue
                path.append(num)
                __backtracker(i,path,target-num)
                path.pop()
        __backtracker(0,[],target)
                




sol = Solution()
candidates = [2,3,6,7], target = 7

