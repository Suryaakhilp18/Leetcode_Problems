class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        #SlidingWindow (Fixed-length sliding window)

        maxAverage = -1000000000

        left = 0

        currentsum = 0


        n = len(nums)

        for right in range(n):
            currentsum += nums[right]
            if right >= k-1:
                avg = currentsum / k
                maxAverage = max(avg,maxAverage)

                #subtracting the value on the left: because the window size exceeds k

                currentsum -= nums[left]
                left += 1

        return maxAverage