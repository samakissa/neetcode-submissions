class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}

        if len(s) != len(t):
            return False
        for x in s:
            seen[x] = seen.get(x,0)+1
        
        for y in t:
            seen[y] = seen.get(y,0)-1
        return all(v == 0 for v in seen.values())