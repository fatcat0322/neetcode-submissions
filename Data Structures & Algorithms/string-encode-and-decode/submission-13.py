class Solution:

    def encode(self, strs: List[str]) -> str:
        enc="".join(f'{len(st)}${st}' for st in strs)
        # enc=''
        # for st in strs:
        #     enc+=(f'{len(st)}${st}')
        return enc
    def decode(self, s: str) -> List[str]:
        dec=[]
        i=0
        while i < len(s):
            j=i
            while s[j] != "$":
                j+=1
            str_len=int(s[i:j])
            i=j+1
            dec.append(s[i:i+str_len])
            i+=str_len
        return dec
            
