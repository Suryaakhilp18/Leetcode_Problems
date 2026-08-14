class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix = 0

        count = 0

        d = {0:1}
        #Because d stores prefix sums we've already seen. At the very beginning, before we process any number, the prefix sum is 0.

        for i in range(len(nums)):
            prefix += nums[i]

            prev = prefix - k

            if prev in d:
                count += d[prev]

            if prefix in d:
                d[prefix] += 1
            else:
                d[prefix] = 1

        return count

        