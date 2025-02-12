def can_partition(nums):
    total_sum=sum(nums)
    if total_sum%2!=0:
       return False
    target=total_sum//2
    dp=[False] * (target+1)
    dp[0]=True
    for num in nums:
        for i in range(target,num-1,-1):
            if dp[i-num] is True:
                dp[i]=True
        if dp[target]:
         return True
    return dp[target]

arr1=[1,5,11,5]
print(f"Array {arr1}:{can_partition(arr1)}")
