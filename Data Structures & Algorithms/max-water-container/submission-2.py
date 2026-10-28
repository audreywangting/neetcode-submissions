class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area = min(height) * width
        # width = right - left 
        # keep moving the shorter bar to see if we could secure the higher bar with bigger area
        # keep maintaining max_area
        max_area = 0
        left = 0
        right = len(heights) -1
        while left < right:
            area = min(heights[left], heights[right]) * (right - left)

            # move the shorter bar
            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1
            max_area = max(max_area, area)

        return max_area



