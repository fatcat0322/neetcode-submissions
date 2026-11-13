class Solution:
    def isValid(self, s: str) -> bool:
        par=[]
        par_dict={'}':'{',']':'[',')':'('}
        for i in range(len(s)):
            if len(par)==0: 
                if (s[i]==')' or s[i]=='}' or s[i]==']'):
                    return False
                else:    
                    par.append(s[i])
            else:
                if s[i] in par_dict.values():
                    par.append(s[i])
                elif par[-1]==par_dict[s[i]]:
                    par.pop()
                else: return False
        return not par
                