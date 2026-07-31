class Solution:
    def thirdMax(self, nums: List[int]) -> int:


        digits = list(set(tuple(nums)))

        digits.sort()

        for i in digits:
            if len(digits) >= 3:
                return digits[-3]

            else:
                return max(digits)