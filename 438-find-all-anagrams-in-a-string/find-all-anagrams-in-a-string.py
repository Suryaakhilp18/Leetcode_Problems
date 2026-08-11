class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        ans = []

        if len(p) > len(s):
            return ans

        p_count = {}

        window = {}

        for ch in p:
            if ch in p_count:
                p_count[ch] += 1

            else:
                p_count[ch] = 1

        for i in range(len(p)):
            if s[i] in window:
                window[s[i]] += 1
            else:
                window[s[i]] = 1

        if window == p_count:
            ans.append(0)

        for i in range(len(p),len(s)):
            left = s[i-len(p)]

            window[left] -= 1

            if window[left] == 0:
                del window[left]

            right = s[i]

            if right in window:
                window[right] +=1
            else:
                window[right] = 1

            if window == p_count:
                ans.append(i-len(p)+1)

        return ans


        
        