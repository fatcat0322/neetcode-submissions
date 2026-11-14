class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans=[0]*len(temperatures)
        stack=[]
        for i,T in enumerate(temperatures):
            while stack and T>temperatures[stack[-1]]:
                prev_i=stack.pop()
                ans[prev_i]=i-prev_i
            stack.append(i)
        return ans
                    
