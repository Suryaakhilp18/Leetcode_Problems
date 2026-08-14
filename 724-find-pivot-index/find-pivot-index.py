class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        prefix = [0]

        sumi = 0

        for i in range(len(nums)):
            sumi += nums[i]

            prefix.append(sumi)

        for i in range(len(nums)):

            leftsum = prefix[i]

            rightsum = prefix[len(nums)] - prefix[i+1]

            if leftsum == rightsum:
                return i

        return -1
        