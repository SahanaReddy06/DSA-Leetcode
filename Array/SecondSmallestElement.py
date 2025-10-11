arr=[12,50,60,28,40]
smallest=arr[0]
ssmallest=float('inf')

for num in arr:
    if num<smallest:
        ssmallest=smallest
        smallest=num
    elif smallest < num < ssmallest:
        ssmallest= num
print("smallest numbers:", smallest)
print("Second smallest", ssmallest)
