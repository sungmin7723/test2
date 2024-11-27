# week13_C_08 1.py

# id:202444105

# name: 윤성민

from datetime import datetime
import os

def diff_seconds(intime, outtime):
    if not outtime:
        outtime = datetime.now()
    return (outtime - intime).total_seconds()

str_fmt = "%Y-%m-%d %H:%M:%S"
mypath = "C:\\book1_202444105"
myfile = "list.txt"
fullfile = os.path.join(mypath, myfile)

if __name__ == "__main__":
    if not os.path.isdir(mypath):
        os.mkdir(mypath)

    books = []

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

        book = {'num': number, 'in': intime, 'out': outtime}
        books.append(book)

    for book in books:
        print(book['num'], book['in'], book['out'])
        print(diff_seconds(book['in'], book['out']))

    with open(fullfile, 'w', encoding="utf-8") as f:
        for book in books:
            num = book["num"]
            intime = datetime.strftime(book["in"], str_fmt)
            outtime = datetime.strftime(book["out"], str_fmt) if book["out"] else ""
            f.write(f"{num}|{intime}|{outtime}\n")

