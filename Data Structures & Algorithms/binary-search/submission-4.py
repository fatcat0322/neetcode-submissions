class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        if nums[l]==target:
            return l
        elif nums[r]==target:
            return r
        while r>l:
            mid=(r-l)//2+l
            print(mid)
            if target==nums[mid]:
                return mid
            elif target==nums[mid+1]:
                return mid+1
            elif target<nums[mid]:
                r=mid-1
            elif target>nums[mid+1]:
                l=mid+1
            else:
                return -1
        return -1
