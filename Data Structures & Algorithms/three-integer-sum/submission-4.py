class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=set()
        for i in range(len(nums)):
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
                    ans.add(tuple([nums[i],nums[l],nums[r]]))
                    l+=1
        return list(ans)