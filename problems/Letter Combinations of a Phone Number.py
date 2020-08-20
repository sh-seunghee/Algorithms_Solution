'''
Letter Combinations of a Phone Number (Medium)

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

'''



'''
1. Resurcive solution

'''
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        alp = 'abcdefghijklmnopqrstuvwxyz'
        alp = list(alp)

        phone = {}
        phone['2'] = alp[0:3]
        phone['3'] = alp[3:6]
        phone['4'] = alp[6:9]
        phone['5'] = alp[9:12]
        phone['6'] = alp[12:15]
        phone['7'] = alp[15:19]
        phone['8'] = alp[19:22]
        phone['9'] = alp[22:26]

        targets = list(digits) # split string into list
        results = []

        def helpCombine(combination, leftoverDigits):

            if not leftoverDigits:
                results.append(combination)
                return
            else:
                for char in phone[leftoverDigits[0]]:
                    # a,b,c
                    helpCombine(combination+char, leftoverDigits[1:])

        helpCombine("", digits)
        return results

S = Solution()
print (S.letterCombinations("23"))