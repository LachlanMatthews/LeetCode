class Solution(object):
    def isValid(self, string):
        brackets = ['(', ')', '{', '}', '[', ']']
        closed = [] #Stores the corresponding closing bracket when the for loop encounters an opening bracket
        for index, bracket in enumerate(string):
            if len(string) % 2 == 0: #Valid string must have an even number of brackets
                if brackets.index(bracket) % 2 == 0: #Checks if current bracket is an opening one
                    closed.insert(0, brackets[brackets.index(bracket) + 1])
                else: #If closing bracket: must match index 0 of closed list
                    if len(closed) != 0:
                        if bracket == closed[0]:
                            closed.pop(0)
                        else:
                            return False
                    else:
                        return False
            else:
                return False
        if len(closed) != 0: #Makes sure closed lsit is empty to checl that all opening brackets were closed
            return False
        return True
        """
        :type string: str
        :rtype: bool
        """
        
# https://leetcode.com/problems/valid-parentheses/

# Takes a string of brackets and determines if they are
# all closed by their matching closing bracket
# "()" "()[]()" "([[[()]]])" "({[([()]([{}]))]})" are all valid
# "(" ")(" "(]" "(([{]}))" are all not valid

#---Constraints
# 1 <= s.length <= 10^4
# s consists of parentheses only '()[]{}'.