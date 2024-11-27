# week13_C_08 1.py

# id:202444105

# name: 윤성민

import book1 
import os
from datetime import datetime as dt

mypath = "c:\\book1_202444105"
myfile = "list.txt"
full_file = mypath + "\\" + myfile
parsingFormat = "%Y-%m-%d %H:%M:%S"

if __name__ == "__main__":
    if not os.path.isdir(mypath):
        os.mkdir(mypath)

    books = []
    if os.path.exists(full_file):
        
        with open(full_file, 'r', encoding = "utf8") as f:
            book_info = f.readlines()
            for line in book_info:
                book_info = line.strip().split('|')
                num = book_info[0]
                intime = dt.strptime(book_info[1], parsingFormat)
                outtime = dt.strptime(book_info[2], parsingFormat) if book_info[2] else None
                book = book1.Book1(num, intime, outtime)
                books.append(book)
            print("복구한 정보입니다.")
            for book in books:
                print(book.num, book.intime, book.outtime)

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
                
        book = book1.Book1(bookno, intime, outtime)
        books.append(book)


    for book in books:
        print(book.num, book.intime, book.outtime)
        print(book.diff_seconds())

    with open(full_file, 'w', encoding = "utf8") as f:
        for book in books:
            num = book.num
            intime = dt.strftime(book.intime, parsingFormat)
            outtime = dt.strftime(book.outtime, parsingFormat) if book.outtime else ""
            f.write(f"{num}|{intime}|{outtime}\n")

