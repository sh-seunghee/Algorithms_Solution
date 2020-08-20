'''
Container with Most Ware (Medium)

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
Note: You may not slant the container and n is at least 2.
'''


'''
1. Brute Force - Time limit exceeded 

Time complexity: O(nxn)
Space complexity: O(1) - Constant extra space is used.

'''
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        tot = 0

        for idx1 in range(len(height)):
            for idx2 in range(idx1+1, len(height)):
                x_len = idx2-idx1
                y_len = min(height[idx1], height[idx2])
                tot = max(tot, x_len * y_len)

        return tot


'''
2. Two Pointer Approach 

This approach is based on the idea that the area formed between the lines will always be limited by the height of the shorter line.
; 다시 생각해보면 two pointer 중에 더 큰 값을 갖는 포인터를 옮기게 될 경우 height는 여전히 더 작은 값을 갖는 포인터에 의해 결정되고 가로축의 길이는 1이 줄기에
결과적으로 더 큰 area를 가질 수 없다. 따라서, two pointer 중에 더 작은 값을 갖는 포인터를 옮긴다.

Time complexity: O(n) - single pass
Space complexity: O(1) - constant space is used

'''
class Solution2(object):
    def maxArea(self, height):

        """
        :type height: List[int]
        :rtype: int
        """
        _max = 0

        pointer1 = 0
        pointer2 = len(height)-1

        # cal space formed by pointer1 and pointer2

        while pointer1 != pointer2:

            x_len = pointer2 - pointer1
            y_len = min(height[pointer1], height[pointer2])

            area = x_len * y_len
            if area > _max:
                _max = area

            if height[pointer1] < height[pointer2]:
                pointer1 += 1
            else:
                pointer2 -= 1

        return _max

S = Solution2()
print (S.maxArea([1,8,6,2,5,4,8,3,7]))


