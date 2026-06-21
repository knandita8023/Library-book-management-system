# Library-book-management-system
To automate library management tasks and provide a simple, user-friendly system for organizing and tracking books.
Description:
The Library Book Management System is a Python-based application used to manage books in a library. It allows users to add, view, issue, and return books. The system helps organize library records efficiently and reduces manual work.
Features:
Add new books
View all books
Search for a book
Issue books to users
Return issued books
Delete books from records
Easy-to-use menu-driven interface
Advantages:
saves time and effort
reduces manual errors
maintains accurate book records
easy book tracking
user friendly system
improves library management efficiency 

code:
library = []

while True:
    print("\n----- Library Management System -----")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

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
sample output:
----- Library Management System -----
1. Add Book
2. View Books
3. Issue Book
4. Return Book
5. Exit

Enter your choice: 1
Enter book name: Python Basics
Book added successfully!

Enter your choice: 2

Available Books:
Python Basics

Enter your choice: 3
Enter book name to issue: Python Basics
Book issued successfully!

Enter your choice: 2
No books available.

Enter your choice: 5
Thank you!

 Future scope:
 Store records permanently using files or databases.
Add login and authentication system.
Track student/member details.
Generate reports of issued and returned books.
Add due-date and fine calculation.
Develop a graphical user interface (GUI).
Convert into a web or mobile application.

Conclusion:
The Library Book Management System is a simple and effective Python project that automates basic library operations and can be expanded into a complete library management solution.
