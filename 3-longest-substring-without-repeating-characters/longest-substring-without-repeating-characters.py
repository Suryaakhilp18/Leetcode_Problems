class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ans = 0
        
        for i in range(len(s)):

            empty = set()

            for j in range(i, len(s)):

                if s[j] in empty:
                    break
                else:
                    empty.add(s[j])
                    cnt = len(empty)

                    ans = max(ans,cnt)
        return ans
                
