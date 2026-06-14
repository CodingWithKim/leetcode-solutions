# @lc app=leetcode id=1512 lang=python3
#
# [1512] Number of Good Pairs
# Category: Array, Hash Table
# Difficulty: Easy
# Link: https://leetcode.com/problems/number-of-good-pairs/
#
# Time Complexity: O(N^2)
# Space Complexity: O(1)
# --------------------------------------------------------
class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        else:
            start, end = 0, 1
            result = 0
            while start < len(nums):
                for i in range(end, len(nums)):
                    if nums[start] == nums[i]:
                        result += 1
                start += 1
                end += 1
            return result

# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.numIdenticalPairs([1,2,3,1,1,3]))    # Output: 4
    print(solution.numIdenticalPairs([1,1,1,1]))        # Output: 6
    print(solution.numIdenticalPairs([1,2,3]))          # Output: 0


