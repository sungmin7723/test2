#week13_C_book.py

class TimeStamp:
    def __init__(self,renttime, returntime):
        self.renttime = renttime
        self.returntime = returntime

    def diff_seconds(self):
        if self.returntime:
            diff = self.returntime - self.renttime
        else:
            diff = dt.now() - self.renttime
            
        return diff.total_seconds()
    
    def is_rent(self):
        return not self.returntime

class Book2:
    def __init__(self, number):
       self.number = number
       self.history = []

       def add_timestamp(self, renttime, returntime):
               self.history.append(TimeStamp(renttime, returntime))
            
