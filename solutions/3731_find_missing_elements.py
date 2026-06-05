# @lc app=leetcode id=3731 lang=python3
#
# [3731] Find Missing Elements
# Category: Array, Hash Table
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-missing-elements/
#
# Time Complexity: O(N log N + M) - where N is len(nums) and M is max(nums) - min(nums)
# Space Complexity: O(N)
# --------------------------------------------------------
class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sorted_nums = sorted(nums)
        start, end = sorted_nums[0], sorted_nums[-1]

        seen = set(nums)
        result = []

        for i in range(start + 1, end):
            if i not in seen:
                result.append(i)

        return result

# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.findMissingElements([1,4,2,5]))    # Output: [3]
    print(solution.findMissingElements([7,8,6,9]))    # Output: []
    print(solution.findMissingElements([5,1]))        # Output: [2,3,4]