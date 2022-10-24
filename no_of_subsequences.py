#A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
ans=[]
def subseq(curr,idx,arr):
    for i in range(idx,len(arr)):
        subs=curr+arr[i]
        ans.append(subs)
        subseq(subs,i+1,arr)
            
subseq("",0,["un","iq","ue"])        
print(ans) 

