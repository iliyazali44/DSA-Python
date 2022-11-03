def mergesort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]
        mergesort(left)
        mergesort(right)
        i=0
        j=0
        k=0
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                arr[k]=left[i]
                i+=1 
            else:
                arr[k]=right[j]
                j+=1 
            k+=1 
        while i<len(left):
            arr[k]=left[i]
            i+=1 
            k+=1 
        while j<len(right):
            arr[k]=right[j]
            j+=1 
            k+=1 
        return arr

print(mergesort([2,13,11,7,2,5,7,1,6,89,2,56]))    

o/p: [1, 2, 2, 2, 5, 6, 7, 7, 11, 13, 56, 89]

