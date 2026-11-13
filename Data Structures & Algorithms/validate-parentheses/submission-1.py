class Solution:
    def isValid(self, s: str) -> bool:
        par=[]
        for i in range(len(s)):
            if len(par)==0: 
                if (s[i]==')' or s[i]=='}' or s[i]==']'):
                    return False
                else:    
                    par.append(s[i])
            else:
                if par[-1]=='(':
                    if s[i]==')':
                        par.pop()
                    elif s[i]=='[' or s[i]=='{' or s[i]=='(':
                        par.append(s[i])
                    else:
                        return False
                elif par[-1]=='[':
                    if s[i]==']':
                        par.pop()
                    elif s[i]=='[' or s[i]=='{' or s[i]=='(':
                        par.append(s[i])
                    else:
                        return False
                elif par[-1]=='{':
                    if s[i]=='}':
                        par.pop()
                    elif s[i]=='[' or s[i]=='{' or s[i]=='(':
                        par.append(s[i])
                    else:
                        return False
        return len(par)==0
                