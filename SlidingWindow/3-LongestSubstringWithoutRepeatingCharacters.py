class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett=set()
        l=0
        max_len=0
        n=len(s)

        for r in range(n):
            while s[r] in sett:
                sett.remove(s[l])
                l+=1
        
            max_len=max(max_len, r-l+1)
            sett.add(s[r])

        return max_len
        
