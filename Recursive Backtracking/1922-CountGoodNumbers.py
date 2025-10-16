class Solution:
    MOD=10**9+7
    def countGoodNumbers(self, n: int) -> int:
        even=(n+1)//2
        odd=n//2

        return (self.pow_mod(5, even)*self.pow_mod(4,odd))%self.MOD
    
    def pow_mod(self, base:int, exp:int)->int:
        if exp==0:
            return 1
        half= self.pow_mod(base, exp//2)
        if exp%2==0:
            return (half*half)%self.MOD
        else:
            return (half*half*base)%self.MOD
        
