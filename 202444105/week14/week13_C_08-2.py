# week13_C_08 2.py

# id:202444105

# name: 윤성민

from datetime import datetime
import os

def diff_seconds(intime, outtime):
    if not outtime:
        outtime = datetime.now()
    return (outtime - intime).total_seconds()

str_fmt = "%Y-%m-%d %H:%M:%S"
mypath = "C:\\book2_202444105"


if __name__ == "__main__":
    if not os.path.isdir(mypath):
        os.mkdir(mypath)

    books = {}

    if not number in books.keys():
        books[number] = []
    else:
        for time in books[number]:
            if time['out'] == None:
                   print("반납을 안 했다")
                   continue
                
        
    while True:
        number = input("도서번호:").strip()
        if not number:
            break
        while True:
            try:
                intime = input("대출시간:").strip()
                if intime:
                    intime = datetime.strptime(intime, str_fmt)
                break
            except:
                pass

        while True:
            try:
                outtime = input("반납시간:").strip()
                if not outtime:
                    outtime = None
                else:
                    outtime = datetime.strptime(outtime, str_fmt)
                break
            except:
                pass

        # book = {'num': number, 'in': intime, 'out': outtime}
        # books.append(book)
        book = {'in': intime, 'out': outtime}
        books[number].append(times)

        book_fullname = os.path.join(mypath, number +  ".txt")
        with open(book_fullname, 'a', encoding = "utf-8") as f:
            intime = dt.strftime(intime, str_fmt)
            if outtime:
                outtime = dt.strftime(outtime, str_fmt)
                f.write(f"{intime}|{outtime}\n")
            else:
                f.write(f"{intime}|")
    for book , times in books.items():
        print("책번호:", number)
        for time in times:
            print(time['num'], time['in'], time['out'])
            print(diff_seconds(time['in'], time['out']))



