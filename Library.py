choice = input("Enter your choice: ")

if choice == '1':
    book = input("Enter book name: ")
    library.append(book)
    print("Book added successfully!")

elif choice == '2':
    if library:
        print("\nAvailable Books:")
        for book in library:
            print(book)
    else:
        print("No books available.")

elif choice == '3':
    book = input("Enter book name to issue: ")
    if book in library:
        library.remove(book)
        print("Book issued successfully!")
    else:
        print("Book not available.")

elif choice == '4':
    book = input("Enter book name to return: ")
    library.append(book)
    print("Book returned successfully!")

elif choice == '5':
    print("Thank you!")
    break

else:
    print("Invalid choice.")
