class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        f=0
        b=len(numbers)-1
        while f<b:
            cur=numbers[f]+numbers[b]
            if cur>target:
                b-=1
            elif cur<target:
                f+=1
            else:
                return [f+1,b+1]
        return None