class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)

        def bin_search(nums, x):
            if not len(nums):
                return -1

            left = 0
            right = len(nums) - 1

            while left < right:
                mid = (left + right) // 2

                if nums[mid] == x:
                    return mid
                if nums[mid] < x:
                    left = mid + 1
                else:
                    right = mid - 1

            if nums[left] == x:
                return left
            return -1

        left = 0
        right = n - 1

        # find min in rotated array
        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        attempt = bin_search(nums[:left], target)
        if attempt != -1:
            return attempt

        attempt = bin_search(nums[left:], target)
        if attempt != -1:
            return left + attempt
        else:
            return -1
