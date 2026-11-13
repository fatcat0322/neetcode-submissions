class MinStack:

    def __init__(self):
        self.stack=[]
        self.mins=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        cur_min=self.mins[-1] if self.mins else val
        if val<=cur_min:
            self.mins.append(min(val,cur_min))

    def pop(self) -> None:
        cur=self.stack.pop()
        if cur==self.mins[-1]:
            self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]
