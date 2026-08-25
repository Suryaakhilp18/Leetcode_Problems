class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans = defaultdict(list)

        for i in strs:
            keys = "".join(sorted(i))
            ans[keys].append(i)
        
        return list(ans.values())