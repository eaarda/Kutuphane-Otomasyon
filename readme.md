##  Library Automation System

A simple flask app for a library automation system. Two roles implemented in this app; user and admin.

------------


### Features

1. This app has 2 different login page. One of them for admins and the other for users.
2. Admin can add new books such as: title, author, type, barcode and status (default:available). That's the point barcode must be unique.
3. Admin can view all the books and search for a book by its title, author or barcode in the system. Admin can delete the books in the system.
4. Admin can manage users. Admin can view all the users currently in the system its username and email but cant view password also can delete users in the system.
5. Users have to create a new account with username,email and password the first time login. If user have a account, can login with email and password.
6. Users can search books by title or author and view all the books in the system its title, author, type and status.
7. If the book's status available, user can borrow the book. Each user can borrow up to 5 books.
8. User can view all the books he/she borrowed, including book title, author, and due date.
9.  Users can delivery books or postpone the due time and also change username and password.

------------

#### Prerequisites
Python3, Python Flask, Sqlite3

- [Install Python for Windows](https://docs.python.org/3/using/windows.html#installation-steps "Install Python for Windows")

- Install Python Flask

` $ pip install Flask`

- Install Sqlite3
	1. First of all, you have to download sqlite3. If you want to download db browser for view the database, can download the second link.

[Download sqlite3](https://www.sqlite.org/download.html "Download sqlite3")

[Download db browser](https://sqlitebrowser.org/ "Download db browser")

	2. Then, you have to create db file in the project file.
	In the terminal,

	`$ sqlite3 data.db`


------------


#### Running Server

`$ python app.py`


------------

#### Note
You have to add a admin for the system.  For this in the terminal,
```shell
python
from app import db
db.create_all()
admin = Admin(admin ='elf', admin_pass= '123')
db.session.add(admin)
db.session.commit()
exit()
```








