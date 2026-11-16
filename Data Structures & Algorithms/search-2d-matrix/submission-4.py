class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        r=len(matrix)-1
        while l<=r:
            mid=(r-l)//2+l
            if  target>=matrix[mid][0]:
                l=mid+1
            else:
                r=mid-1
        m=r
        l=0
        r=len(matrix[0])-1
        while l<=r:
            mid=(r-l)//2+l
            if target==matrix[m][mid]:
                return True
            elif target<matrix[m][mid]:
                r=mid-1
            else:
                l=mid+1
        return False