# 4. Write a python program which will keep track of the stock of books available in the library. 
# In this program, you will have to use the add( ) to add the books, and also the display( ).
from datetime import date
import os
class Library:
    __bookId = 1000
    total_book = 0
    __book_list = {}
    def add():
        title = input("\tEnter Book Title : ")
        author = input("\tEnter Author Name : ")
        qty = int(input("\tNo of books : "))
        
        for bookId,book_list in Library.__book_list.items():
            if book_list["author"]==author and book_list["title"]==title:
                book_list["qty"] += qty
                book_list["date"] = date.today()
                print("\n\t\tBook Added...")
                return
            
        Library.__bookId = Library.__bookId+1
        Library.__book_list[Library.__bookId] = {"title":title,"author":author,"qty":qty,"date":date.today()}
        print("\n\t\tBook Added...")
    
    def show():
        if len(Library.__book_list)==0:
            print("\n\t\tNo book found.")
            return
        print("\n\n\t\t..........List of Books Available in Library..........\n\n")
        for bookId,book_list in Library.__book_list.items():
            print("\n\n\tBook Id : ",bookId)
            print("\tTitle : ",book_list["title"])
            print("\tAuthor : ",book_list["author"])
            print("\tQuantity Avl : ",book_list["qty"])
            print("\tAdded on : ",book_list["date"])
            
    def search():
        bookId = int(input("\tEnter Book Id : "))
        if bookId in Library.__book_list.keys():
            book_list = Library.__book_list[bookId]
            print("\n\n\tBook Id : ",bookId)
            print("\tTitle : ",book_list["title"])
            print("\tAuthor : ",book_list["author"])
            print("\tQuantity Avl : ",book_list["qty"])
            print("\tAdded on : ",book_list["date"])
        else:
            print("\n\t\tNo book found.")


flag = True
while(flag):
    print("\n\t\tVIDYASAGAR UNIVERSITY (Library Management System)\n\n")
    print("\n\tPress 1 : Add Book\tPress 2 : Show Books\n\tPress 3 : Search Book\tPress 4 : Exit")
    n = int(input())
    os.system('cls')
    print("\n\t\tVIDYASAGAR UNIVERSITY(Library Management System)\n\n")
    if n==1:
        Library.add()
        input()
        os.system('cls')
    elif n==2:
        Library.show()
        input()
        os.system('cls')
    elif n==3:
        Library.search()
        input()
        os.system('cls')
    elif n==4:
        flag = False
    else:
        print("\n\t\tWrong Choice. Try Again..")
        input()
        os.system('cls')