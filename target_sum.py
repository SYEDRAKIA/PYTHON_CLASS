def two_sum(nums,target):
    seen={}

    for i,num in enumerate(nums):
        complement=target-num
        if complement in seen:
            return [seen[complement],i]
        seen[num]=i
    return []

nums=[2,11,7,15]
target=9
print(two_sum(nums,target))