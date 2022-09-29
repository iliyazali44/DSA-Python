def maxSubarraySum(arr, n) :

	# Your code here
    # return the answer
    maxsum=0
    sum=0
    for i in range(n):
        sum+=arr[i]
        maxsum=max(maxsum,sum)
        if sum<=0:
            sum=0
    return maxsum
