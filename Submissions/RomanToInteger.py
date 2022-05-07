class Solution(object):
    def romanToInt(self, s):
        symbols = ['I','V','X','L','C','D','M']
        values = [1,5,10,50,100,500,1000]
        result = 0
        for x in range(len(s)):
            if x != len(s) - 1:
                if symbols.index(s[x]) < symbols.index(s[x + 1]):
                    result -= values[symbols.index(s[x])]
                else:
                    result += values[symbols.index(s[x])]
            else:
                result += values[symbols.index(s[x])]
        return result
        """
        :type s: str
        :rtype: int
        """

# https://leetcode.com/problems/roman-to-integer/

# romanToInt() takes a string that contains a roman
# numeral and then converts it to the number that
# it represents

#---Constraints
# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].