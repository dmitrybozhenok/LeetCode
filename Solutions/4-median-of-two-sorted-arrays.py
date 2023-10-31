from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i,k=0,0
        len1 = len(nums1)
        len2 = len(nums2)
        nums = []
        while i < len1 and k < len2:
            if nums1[i] < nums2[k]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[k])
                k += 1
        if i == len1:
            for el in nums2[k:]:
                nums.append(el)
        else:
            for el in nums1[i:]:
                nums.append(el)

        if len(nums) % 2 == 0:
            return (nums[len(nums)//2] + nums[len(nums)//2 - 1])/2
        else:
            return nums[len(nums)//2]

solution = Solution()
ret = solution.findMedianSortedArrays([1,3],[2])