books = ["The Alchemist", "1984", "Moby Dick", "Pride and Prejudice"]
books.append("The Cruel Prince")
books.append("The Last Culling")
books.remove("1984")
books.sort()
print(books)

borrower_info = ({name}: {library_id}: {membership_date})
name = input('Please input your name e.g "John Doe": ').title()
library_id = input('Please enter your library ID e.g B1023: ')
membership_date = int(input(
    'Please enter the day you joined, e.g 2025-10-15: '))

print(len(borrower_info))
