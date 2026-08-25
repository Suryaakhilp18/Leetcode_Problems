class Solution:
    def findNumbers(self, nums: List[int]) -> int:

        answer = 0

        for i in nums:
            if len(str(i)) % 2 == 0:
                answer += 1
        return answer