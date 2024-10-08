class Solution:
    def search(self, nums, target):

        start = 0
        end = len(nums) - 1

        while (start <= end):
            mid = start + (end - start) // 2

            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                start = mid + 1
            if target < nums[mid]:
                end = mid - 1
        return -1