class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n <= 0:
            return False

        while n % 2 == 0:
            n //= 2
        return n == 1 #-->if u keep dividing and last if u get 1 , then it is a power of 2
        