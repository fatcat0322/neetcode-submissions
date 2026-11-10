class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_num={}
        for i,s in enumerate(strs):
            char_freq=[0 for i in range(26)]
            for c in s:
                char_freq[ord(c)-ord('a')]+=1
            if tuple(char_freq) in ana_num:
                ana_num[tuple(char_freq)].append(s)
            else:
                ana_num[tuple(char_freq)]=[s]
        out=[]
        for v in ana_num.values():
            out.append(v)
        return out