class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while r>l:
            mid=(r-l)//2+l
            print(mid)
            if target==nums[mid]:
                return mid
            elif target<nums[mid]:
                r=mid-1
            elif target>nums[mid]:
                l=mid+1
        return r if nums[r]==target else -1
