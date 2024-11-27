# week13_C_08 1.py

# id:202444105

# name: 윤성민

import os
from datetime import datetime as dt

mypath = "c:\\book1_202444105"
myfile = "list.txt"
full_file = mypath + "\\" + myfile
parsingFormat = "%Y-%m-%d %H:%M:%S"

def diff_seconds(intime, outtime):
        if not outtime:
            outtime = dt.now()
        ds = outtime - intime
        return ds.total_seconds()

if __name__ == "__main__":
    if not os.path.isdir(mypath):
        os.mkdir(mypath)

    books = []
    if os.path.exists(full_file):
        with open(full_file, 'r', encoding = "utf8") as f:
            b = f.readlines()
            for line in b:
                book_info = line.strip().split('|')
                num = book_info[0]
                intime = dt.strptime(book_info[1], parsingFormat)
                outtime = dt.strptime(book_info[2], parsingFormat) if book_info[2] else None
                book = {'num': num, 'in': intime, 'out': outtime}
                books.append(book)
        print('복구한 정보입니다.')
        for book in books:
            print(book['num'], book['in'], book['out'])  

    while True:
        bookno = input("도서번호 : ").strip()
        if not bookno:
            break
        while True:
            try:
                intime = input("대출시간 : ").strip()
                if intime:
                    intime = dt.strptime(intime, parsingFormat)
                    break
            except:
                pass

        while True:
            try:
                outtime = input("반납시간 : ").strip()
                if outtime:
                    outtime = dt.strptime(outtime, parsingFormat)
                else:
                    outtime = None
                break
            except:
                pass
                
        book = {'num': bookno, 'in': intime, 'out': outtime}
        books.append(book)


    for book in books:
        print(book['num'], book['in'], book['out'])
        print(diff_seconds(book["in"], book["out"]))

    with open(full_file, 'w', encoding = "utf8") as f:
        for book in books:
            num = book['num']
            intime = dt.strftime(book['in'], parsingFormat)
            outtime = dt.strftime(book['out'], parsingFormat) if book['out'] else ""
            f.write(f"{num}|{intime}|{outtime}\n")
