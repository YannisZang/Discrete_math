
def sort_books(books):
    day = 0

    for i in range(len(books)):
        j = books.index(i)
        if j != i:
            books[i], books[j] = books[j], books[i]
            print(f'After day {day}: {books}')
            day += 1


sort_books([0, 5, 8, 1, 2, 3, 7, 4, 9, 6])