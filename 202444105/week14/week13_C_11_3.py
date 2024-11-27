# week13_C_11_3.py

# id:202444105

# name: 윤성민
from week13_C_book import Book2 as Book
from week13_C_book import TimeStamp
from datetime import datetime as dt
import datetime
import os

str_fmt = "%Y-%m-%d %H:%M:%S"
mypath = "C:\\book2_202444105"

if __name__ == "__main__":
    if not os.path.isdir(mypath):
        os.mkdir(mypath)

    books = []
    members = os.listdir(mypath)
    
    for member in members:
        member_fullname = os.path.join(mypath, member)
        if os.path.isfile(member_fullname):
            file_ext = os.path.splitext(member)
            if file_ext and len(file_ext) == 2 and file_ext[-1] == ".txt":
                number = file_ext[0].strip()
                books[number] = []
                with open(book_fullname, 'a', encoding = "utf-8") as f:
                    for line in f:
                        split_datas = line.strip().split('|')
                        if split_datas and len(split_datas) == 2:
                            intime = dt.strptime(split_datas[0], str_fmt)
                            if split_datas[1].strip():
                                outtime = dt.strptime(split_datas[1].strip(), str_fmt)
                            else:
                                outtime = None
                            books.add_timestamp(intime, outtime)
                if book.history:
                    book
    
                search
        
    while True:
        number = input("도서번호:").strip()
        if not number:
            break

        search_book = [book for book in books if book.number == number]
        
        if not search_book:
            book = Book(number)
            books.append(book)
        else:
            book = search_book[0]
            for timestamp in book.history:
                if timestamp.is_rent():
                    print("반납을 안 했다")
                    continue
            
                
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

        # book = {'in': intime, 'out': outtime}
        # books[number] = []
        book.add_timestamp(intime, outtime)

        book_fullname = os.path.join(mypath, number +  ".txt")
        with open(book_fullname, 'a', encoding = "utf-8") as f:
            intime = dt.strftime(intime, str_fmt)
            if outtime:
                outtime = dt.strftime(outtime, str_fmt)
                f.write(f"{intime}|{outtime}\n")
            else:
                f.write(f"{intime}|")
    for book in books:
        print("책번호:", number)
        for timestamp in book.history:
            print(timestamp.renttime, timestmap.returntime)
            print(timestamp.diff_seconds())



