'''
Two Sum (Easy)

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''


'''
1. Brute Force

Time complexity: O(nxn) 
Space complexity: O(1)

'''
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):

                if target == nums[i] + nums[j]:
                    return [i, j]


'''
2. Hash Table

While we iterate and insert elements into the table, we also look back to check if current element's complement already exist in the table.
if it exists, we have found a solution and return immediately.

Time Complexity: O(n) - We traverse the list containing n elements only once. Each look up in the table costs only O(1) time.
Space complexity: O(n) - The extra space required depends on the number of items stored in the hash table, which stores at most n elements

'''

class Solution2:
    def twoSum(self, nums, target):
        '''
        :param nums: List[int]
        :param target: int
        :return: List[int]
        '''

        h = {}
        for i, num in enumerate(nums):
            n = target - num

            if n not in h:
                h[num] = i
            else:
                return [h[n], i]

