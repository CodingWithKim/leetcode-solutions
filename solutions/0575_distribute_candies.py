# @lc app=leetcode id=575 lang=python3
#
# [575] Distribute Candies
# Category: Array, Hash Table
# Difficulty: Easy
# Link: https://leetcode.com/problems/distribute-candies/
#
# Time Complexity: O(N)
# Space Complexity: O(N)
# --------------------------------------------------------
class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        unique = list(set(candyType))
        can_eat = len(candyType) // 2

        return len(unique[:can_eat])

# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.distributeCandies([1,1,2,2,3,3]))  # Output: 3
    print(solution.distributeCandies([1,1,2,3]))      # Output: 2
    print(solution.distributeCandies([6,6,6,6]))      # Output: 1