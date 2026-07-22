books = ["The Alchemist", "1984", "Moby Dick", "Pride and Prejudice"]
books.append("The Cruel Prince")
books.append("The Last Culling")
books.remove("1984")
books.sort()
print(books)


name = input('Please input your name e.g "John Doe": ').title()
library_id = input('Please input your library ID e.g B1023: ')
day = int(input('Please input the day you joined: '))
month = int(input('Please input the month you joined: '))
year = int(input('Please input the year you joined: '))
membership_date = (f'{year}-{month:02}-{day:02}')
borrower_info = (name, library_id, membership_date)
print(len(borrower_info))
borrower_info[0] = 'Riley Davis'
print(borrower_info)
for info in borrower_info:
    print(info)


title = "The Cruel Prince"
author = "Holly Black"
publication_year = 2018
book_info = (title, author, publication_year)
title, author, publication_year = book_info
