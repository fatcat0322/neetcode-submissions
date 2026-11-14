class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        longest=0
        cnt=0
        cars=sorted(zip(position,speed),reverse=True)
        for p,s in cars:
            t=(target-p)/s
            if t>longest:
                longest=t
                cnt+=1
        
        return cnt