class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        f=1
        b=len(numbers)
        while f<b:
            if numbers[f-1]+numbers[b-1]>target:
                b-=1
            elif numbers[f-1]+numbers[b-1]<target:
                f+=1
            else:
                return [f,b]
        return None