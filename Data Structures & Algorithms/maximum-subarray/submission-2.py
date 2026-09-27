class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        running_sum = 0
        for n in nums:
            if running_sum < 0:
                running_sum = 0
            running_sum += n
            if running_sum > max_sum:
                max_sum = running_sum
        return max_sum