class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        zeroscnt = 0
        maxlength = 0
        left = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeroscnt += 1

            while zeroscnt > k:
                if nums[left] == 0:
                    zeroscnt -= 1
                left += 1

            maxlength = max(maxlength,right-left+1)

        return maxlength

        
        