class Solution:
    def dominantIndex(self, nums: List[int]) -> int:

        lst = list(nums)
        nums.sort()

        if nums[-2] * 2 <= nums[-1]:
            return lst.index(nums[-1])

        return -1


        