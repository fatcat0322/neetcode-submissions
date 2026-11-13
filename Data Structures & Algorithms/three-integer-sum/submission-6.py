class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        if nums[0]>0: return []
        ans=[]
        for i in range(len(nums)):
            if i>0 and nums[i-1]==nums[i]:
                continue
            l=i+1
            r=len(nums)-1
            target=0-nums[i]
            while l<r:
                cur=nums[l]+nums[r]
                if cur<target:
                    l+=1
                elif cur>target:
                    r-=1
                else:
                    ans.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
        return ans