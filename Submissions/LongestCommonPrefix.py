class Solution(object):
    def longestCommonPrefix(self, words):
        prefix = words[0]
        prefixChars = prefix.split()
        words.pop(0)
        match = 0
        for word in words:
            for count, char in enumerate(word):
                try:
                    if char == prefix[count]:
                        match += 1
                    else:
                        break
                except:
                    pass
            prefix = prefix[:match]
            match = 0
        return prefix
        """
        :type strs: List[str]
        :rtype: str
        """

# https://leetcode.com/problems/longest-common-prefix/

# longestCommonPrefix() takes a list of words and determines
# the longest substring of word found at the start of each
# word in the list

#---Constraints
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lower-case English letters.