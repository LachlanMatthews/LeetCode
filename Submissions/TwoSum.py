class Solution(object):
    def twoSum(self, nums, target):
        index1 = 0
        index2 = 0
        for i in nums:
            for j in nums:
                if index1 != index2:
                    if i + j == target:
                        answer = [index1, index2]
                        return answer
                index2 += 1
            index1 += 1
            index2 = 0
                
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

# twoSum() takes a list of integers and a target number.
# The function finds two numbers in a list that will 
# add up to the target and then returns the answer
# in an integer list