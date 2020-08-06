class Logger:

    def __init__(self):
        self.dict_ = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        dict_ = self.dict_

        if message not in dict_.keys():
            dict_[message] = timestamp
            return True

        if (timestamp - dict_[message]) >= 10:
            dict_[message] = timestamp
            return True
        else:
            return False
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)

if __name__ == "__main__":
    obj = Logger()
    obj.shouldPrintMessage(1,'foo')
    obj.shouldPrintMessage(2,'bar')
    obj.shouldPrintMessage(3,'foo')
    obj.shouldPrintMessage(8,'bar')
    obj.shouldPrintMessage(10,'foo')
    obj.shouldPrintMessage(11,'foo')
