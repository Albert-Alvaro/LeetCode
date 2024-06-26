class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        max_a = 0
        left = 0
        right = len(height) - 1

        while left < right:
            area = min(height[left], height[right]) * (right-left)
            max_a = max(max_a, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_a
    

print(Solution.maxArea("", [1,8,6,2,5,4,8,3,7]))
