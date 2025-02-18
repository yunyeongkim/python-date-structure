class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        if n == 0:
            return None
        for i in range(m, m+n):
            nums1[i] = nums2[m-i]
        nums1.sort()


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

sol = Solution()
sol.merge(nums1,m,nums2,n)


nums1 = [1]
m = 1
nums2 = []
n = 0

sol = Solution()
sol.merge(nums1,m,nums2,n)

nums1 = [0]
m = 0
nums2 = [1]
n = 1

sol = Solution()
sol.merge(nums1,m,nums2,n)