#recurrsive approach
def binarysearch(arr,start,end,ele):
    if start>end:
        return -1
    else:  
      mid=(start+end)//2
      if arr[mid]==ele:
          return mid
      elif arr[mid]>ele:
          return binarysearch(arr,start,mid-1,ele)
      elif arr[mid]<ele:
          return binarysearch(arr,mid+1,end,ele)
    
#iterative approach
def binarysearch(arr,start,end,ele):
    while(start<=end):
        mid=(start+end)//2 
        if arr[mid]==ele:
            return mid
        elif arr[mid]>ele:
            end=mid-1
        elif arr[mid]<ele:
            start=mid+1 
    return -1        

x=[1,3,5,7,9,12,45,78,90]
n=len(x)-1
print(binarysearch(x,0,n,1))
