# @lc app=leetcode id=3289 lang=python3
#
# [3289] The Two Sneaky Numbers of Digitville
# Category: Array, Hash Table
# Difficulty: Easy
# Link: https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/
#
# Time Complexity: O(N)
# Space Complexity: O(N)
# --------------------------------------------------------
class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen = set()
        appear_twice = []

        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                appear_twice.append(num)

        return appear_twice

# Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Important Note: Sequence does not matter for this question!!!
    print(solution.getSneakyNumbers([0,1,1,0]))                   # Output: [0,1]
    print(solution.getSneakyNumbers([0,3,2,1,3,2]))               # Output: [2,3]
    print(solution.getSneakyNumbers([7,1,5,4,3,4,6,0,9,5,8,2]))   # Output: [4,5]