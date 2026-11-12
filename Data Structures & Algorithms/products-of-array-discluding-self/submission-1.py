class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fw_products=[1]
        bk_products=[1]
        fwp=1
        bkp=1
        for i in range(len(nums)-1):
            fwp*=nums[i]
            bkp*=nums[-i-1]
            fw_products.append(fwp)
            bk_products.append(bkp)
        ans=[]
        for i in range(len(nums)):
            ans.append(fw_products[i]*bk_products[-i-1])
        return ans 