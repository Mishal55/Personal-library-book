import json
import os

data = 'library.txt'

def load_library():
    if os.path.exists(data):
        with open(data, 'r') as file:
            return json.load(file)
    return []

def save_library(library):
    with open(data, 'w') as file:
        json.dump(library, file, indent=4)

def add_book(library):
    title = input('Enter the title of the book: ')
    author = input('Enter the author of the book: ')
    year = input('Enter the year of the book: ')
    genre = input('Enter the genre of the book: ')
    read = input('Have you read the book (yes/no)? ').lower() == 'yes'

    new_book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }

    library.append(new_book)
    save_library(library)
    print(f'Book "{title}" added successfully.')

def remove_book(library):
    title = input("Enter the title of the book to remove: ").lower()
    initial_length = len(library)
    library[:] = [book for book in library if book['title'].lower() != title]

    if len(library) < initial_length:
        save_library(library)
        print(f'Book "{title}" removed successfully.')
    else:
        print(f'Book "{title}" not found in the library.')

def search_book(library):
    search_by = input("Search by title or author: ").lower()
    search_term = input(f'Enter the {search_by}: ').lower()

    result = [book for book in library if search_term in book.get(search_by, '').lower()]

    if result:
        for book in result:
            status = 'Read' if book['read'] else 'Unread'
            print(f"{book['title']} by {book['author']} - {book['genre']} - {status}")
    else:
        print(f"No books found matching '{search_term}' in the {search_by} field.")

def display_all_books(library):
    if not library:
        print('The library is empty.')
        return

    for book in library:
        status = 'Read' if book['read'] else 'Unread'
        print(f"{book['title']} by {book['author']} - {book['year']} - {book['genre']} - {status}")

def display_statistics(library):
    total_books = len(library)
    read_books = sum(1 for book in library if book['read'])
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0

    print(f"Total books: {total_books}")
    print(f"Books read: {read_books}")
    print(f"Percentage read: {percentage_read:.2f}%")

def library_system():
    library = load_library()

    while True:
        print("Wellcome to the Library Manage")
        print("\nMenu:")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Display All Books")
        print("5. Display Statistics")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_book(library)
        elif choice == '4':
            display_all_books(library)
        elif choice == '5':
            display_statistics(library)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
library_system()
