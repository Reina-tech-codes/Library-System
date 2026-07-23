# Question 1
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
for info in borrower_info:
    print(info)


title = "The Cruel Prince"
author = "Holly Black"
publication_year = 2018
book_info = (title, author, publication_year)
title, author, publication_year = book_info
print(f'Title: {title}')
print(f'Author: {author}')
print(f'Publication Year: {publication_year}')

borrowed_books = [23, 19, 31, 27, 22, 30, 25]
weekly_records = borrowed_books[1:5]
borrowed_books[0] = 20
print(weekly_records)
print(borrowed_books)
