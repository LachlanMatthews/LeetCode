class Solution(object):
    def isPalindrome(self, x):
        numString = str(x)
        check = 0
        count = 1
        for x in numString:
            if x == numString[len(numString) - count]:
                check += 1
            count += 1
        if check == len(numString):
            return True
        else:
            return False
        """
        :type x: int
        :rtype: bool
        """

# https://leetcode.com/problems/palindrome-number/

# isPalindrome() is given an int to determine if
# it is a palindrome number. Returns true if it is
# and false if it isn't

#---Constraints
# -2^31 <= x <= 2^31 - 1