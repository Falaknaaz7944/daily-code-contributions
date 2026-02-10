nums = [1, 1, 2, 2, 2, 3, 1]
n=len(nums)
count=0
for i in range(1,n):
    if nums[i]!=nums[i-1]:
        count+=1
        
print(count)


