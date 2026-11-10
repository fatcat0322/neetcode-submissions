class Solution:

    def encode(self, strs: List[str]) -> str:
        enc=''
        for i,st in enumerate(strs):
            str_len=len(st)
            enc+=(f'{str_len}${st}')
        print(enc)
        return enc

    def decode(self, s: str) -> List[str]:
        dec=""
        ans=[]
        cnt=""
        str_len=0
        ch_flag=False
        for ch in s:
            if not ch_flag:
                cnt+=ch
            # print("ch "+ch)
            # print("cnt "+cnt)
            if ch == "$" and not ch_flag:
                try:
                   str_len=int(cnt[:-1])
                except ValueError:
                    continue
                ch_flag = True
                print('str_len '+str(str_len))
                if str_len == 0:
                    ans.append("")
                    print("ans "+str(ans))
                    ch_flag=False
                cnt=""
            elif ch_flag and str_len != 0:
                dec+=ch
                str_len-=1                
                # print('str_len '+str(str_len))
                if str_len==0:
                    ans.append(dec)
                    # print('dec '+dec)
                    dec=""
                    ch_flag=False
        return ans