class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[1]
        fwp=1
        for i in range(0,len(nums)-1,1):
            fwp*=nums[i]
            ans.append(fwp)
        fwp=1
        for i in range(len(nums)-1,-1,-1):
            ans[i]*=fwp
            fwp*=nums[i]
        return ans