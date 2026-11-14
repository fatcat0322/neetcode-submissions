class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans=[0]*len(temperatures)
        stack=[]
        for i,T in enumerate(temperatures):
            if not stack or T<=temperatures[stack[-1]]:
                stack.append(i)
            elif T>temperatures[stack[-1]]:
                while stack and T>temperatures[stack[-1]]:
                    prev_i=stack.pop()
                    ans[prev_i]=i-prev_i
                stack.append(i)
        return ans
                    
