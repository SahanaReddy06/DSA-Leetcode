class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        count=defaultdict(int)                     #Frequency of each character in the current window
        l=0
        n=len(s)
        max_len=0
        max_freq=0                                 #Highest frequency of a single character in the window

        for r in range(n):
            count[s[r]]+=1
            max_freq=max(max_freq, count[s[r]])

            while (r-l+1) - max_freq > k :
                count[s[l]]-=1
                l+=1
            max_len=max(max_len, r-l+1)
        return max_len
        
