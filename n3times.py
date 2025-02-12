def fxn(nums):
    n=len(nums)
    freq={} 
    result=[]

    for num in nums:
        freq[num]=freq.get(num,0)+1
    for num,count in freq.items():
        if count > n//3:
            result.append(num)
    return result

nums=[3,2,3,2,2,1,1,1,1,2]
print(fxn(nums))
