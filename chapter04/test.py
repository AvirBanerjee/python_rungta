nums=[2,3,4,5,7,8]
n=len(nums)
target=7

st=0
end=n-1

mid=(end-st)//2
while(st<end):
    if(nums[mid]==target):
        print(mid)
        break
    if(nums[mid]<target):
        st=mid+1
    else:
        end=mid+1  
    mid=(st+end)//2;       
