class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.list_ = []
        self.window_sum = 0
        

    def next(self, val: int) -> float:
        size, list_= self.size, self.list_
        list_.append(val)
        tail = 0
        if len(list_) > size:
            tail = list_.pop(0)
        self.window_sum = self.window_sum - tail + val
        return self.window_sum/len(list_)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

if __name__ == '__main__':
    obj = MovingAverage(3)
    obj.next(1)
    obj.next(10)
    obj.next(3)
    obj.next(5)


