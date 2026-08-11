class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        window = sum(arr[:k])

        count  = 0
        # Check first window
        if window >= k * threshold:
            count += 1
        #since first k elements are already inside our window
        for i in range(k,len(arr)):
            window += arr[i]
            window -= arr[i-k]

            if window >= k * threshold:
                count += 1

        return count
        