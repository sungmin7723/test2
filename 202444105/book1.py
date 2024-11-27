# week13_C_08 1.py

# id:202444105

# name: 윤성민

from datetime import datetime as dt

class Book1 :
    def __init__(self, num, intime, outtime):
        self.num=num
        self.intime=intime
        self.outtime=outtime
    

    def diff_seconds(self):
        if not self.outtime:
            outtime = dt.now()
            
        return (outtime - self.intime).total_seconds()