class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        prefix_sum = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]
            result.append(prefix_sum)

        return result

solution = Solution()
print(solution.runningSum([1,2,3,4]))
