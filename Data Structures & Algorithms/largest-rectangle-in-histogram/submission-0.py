class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        stack = [] #(index, height) pair

        for i, h in enumerate(heights):
            #left boundry for each bar
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                width = i - index
                area = max(area, width * height)
                start = index

            stack.append((start, h))

        for i, h in stack:
            w = len(heights) - i
            area = max(area, w * h)
            
        return area