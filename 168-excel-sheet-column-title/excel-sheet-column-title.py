class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        ans = []

        while columnNumber > 0:

            columnNumber -= 1

            ans.append(chr(columnNumber % 26 + ord('A')))

            columnNumber //= 26

        return "".join(ans[::-1])

#columnNumber = 28

#28 - 1 = 27
#27 % 26 = 1 → B
#27 // 26 = 1

#1 - 1 = 0
#0 % 26 = 0 → A
#0 // 26 = 0

#Collected = [B,A]
#Reverse → "AB"
        