class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l_idx=0
        r_idx=len(nums)-1
        if target>nums[r_idx] or target<nums[l_idx]:
            return -1
        elif target==nums[l_idx]:
            return l_idx
        elif target==nums[r_idx]:
            return r_idx
        while target<nums[r_idx] and target>nums[l_idx]:
            mid=(r_idx-l_idx)//2+l_idx
            if target==nums[mid]:
                return mid
            elif target==nums[mid+1]:
                return mid+1
            elif target<nums[mid]:
                r_idx=mid
            else:
                l_idx=mid+1
        return -1
