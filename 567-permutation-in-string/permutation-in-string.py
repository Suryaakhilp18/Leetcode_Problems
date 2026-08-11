class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        p_count = {}
        window = {}

        for ch in s1:
            if ch in p_count:
                p_count[ch] += 1
            else:
                p_count[ch] = 1

        for i in range(len(s1)):
            if s2[i] in window:
                window[s2[i]] += 1
            else:
                window[s2[i]] = 1

        if window == p_count:
            return True

        for i in range(len(s1), len(s2)):
            left = s2[i - len(s1)]

            window[left] -= 1

            if window[left] == 0:
                del window[left]

            right = s2[i]

            if right in window:
                window[right] += 1
            else:
                window[right] = 1

            if window == p_count:
                return True

        return False