class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # set heights[i] = left bar, heights[j] = right bar
        # area = height * width
        # height = min(height), width = j - i
        # goal: to find the max area by moving the shorter bar
        # since taller bar may secure more area

        i = 0
        j = len(heights) - 1
        max_area = 0
        while i < j:
            area = min(heights[i], heights[j])*(j-i)

            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1

            max_area = max(area, max_area)

        return max_area

