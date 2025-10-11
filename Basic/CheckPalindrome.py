s="abccba"
left=0
right=len(s)-1
while left < right:
    if s[left]!=s[right]:
        print("not a palindrome")
    left+=1
    right-=1
else:
    print("its a palindrome")
