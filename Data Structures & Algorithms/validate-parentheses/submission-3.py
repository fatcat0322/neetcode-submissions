class Solution:
    def isValid(self, s: str) -> bool:
        par=[]
        par_dict={'}':'{',']':'[',')':'('}
        for i in s:
            if len(par)==0: 
                if i in par_dict:
                    return False
                else:    
                    par.append(i)
            else:
                if i in par_dict.values():
                    par.append(i)
                elif par[-1]==par_dict[i]:
                    par.pop()
                else: return False
        return not par
                