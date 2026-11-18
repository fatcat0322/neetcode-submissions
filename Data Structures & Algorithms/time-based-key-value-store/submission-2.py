class TimeMap:

    def __init__(self):
        self.TM=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.TM[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        series=self.TM.get(key,[])
        l=0
        r=len(series)-1
        while l<=r:
            mid=(r-l)//2+l
            if series[mid][0]<=timestamp:
                l=mid+1
            else:
                r=mid-1
        return "" if r<0 else series[r][1]
