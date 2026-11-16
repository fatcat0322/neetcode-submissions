class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        r=len(matrix)-1
        found=False
        while l<=r:
            mid=(r-l)//2+l
            if target<=matrix[mid][-1] and target>=matrix[mid][0]:
                m=mid
                found=True
                break
            elif target<matrix[mid][0]:
                r=mid-1
            else:
                l=mid+1
        print('m found')
        if found:
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