class Solution:
    def isValid(self, s: str) -> bool:
        par=[]
        par_dict={'}':'{',']':'[',')':'('}
        for i in s:
            if i in par_dict:
                if (not par) or par[-1]!=par_dict[i]:
                    return False
                par.pop()
            else: par.append(i)
        return not par
                