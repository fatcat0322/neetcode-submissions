class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        mat_l=[]
        for row in matrix:
            mat_l.extend(row)
        l=0
        r=len(mat_l)-1
        while l<=r:
            mid=(r-l)//2+l
            if target==mat_l[mid]:
                return True
            elif target<mat_l[mid]:
                r=mid-1
            else:
                l=mid+1
        return False