class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        t_stack=[]
        sort=sorted(zip(position,speed),reverse=True)
        for p,s in sort:
            t=(target-p)/s
            if not t_stack or t>t_stack[-1]:
                t_stack.append(t)
        
        return len(t_stack)