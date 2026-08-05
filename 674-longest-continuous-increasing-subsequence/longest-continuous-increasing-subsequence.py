class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:

        count = 1

        ans = 1

        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                count += 1
            else:
                count = 1

            ans = max(ans,count)
            
        return ans
        