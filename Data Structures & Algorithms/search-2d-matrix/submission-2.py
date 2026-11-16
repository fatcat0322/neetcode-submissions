class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        l=0
        r=m*n-1
        while l<=r:
            mid=(r-l)//2+l
            mid_m=mid//n
            mid_n=mid%n
            if target==matrix[mid_m][mid_n]:
                return True
            elif target<matrix[mid_m][mid_n]:
                r=mid-1
            else:
                l=mid+1
        return False