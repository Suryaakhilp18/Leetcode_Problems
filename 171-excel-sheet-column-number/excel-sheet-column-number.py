class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        res = 0

        for ch in columnTitle:
            #-->convert letter into a num
            value = ord(ch) - ord('A') + 1
            #--->Similar to decimal (×10), here we use ×26.
            res = res * 26 + value

        return res


