class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        lst = []
        sumi = 0
        for i in nums:
            sumi += i
            lst.append(sumi)
        return lst


        