import csv
with open('books.csv','rt') as fin:
    cin = csv.DictReader(fin)
    books = [row for row in cin]

print(books)