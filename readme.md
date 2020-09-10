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

## Prerequisites
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


### Running Server

`$ python app.py`


------------

### Note
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


------------

## Database Schema

A database schema is the blueprints of your database, it represents the description of a database structure, data types, and the constraints on the database.  As you can see in this project, database has 5 tables.

![](https://github.com/eaarda/Library-Automation-System/blob/master/ss/dia.png)

------------
## API Documentation

**1.  POST -  /authentication**

It verifies the identity of the user.  It gives the user the authority to use the service.

**Request**

| Params  | Value |
| ------------ | ------------ |
|  email  | string User.email  |
| password  | string User.password   |


**2. GET - /authentication**

It terminates the user's authority to access the service.

**3. POST -  /register**

It registers a new user.

**Request**

| Params  | Value |
| ------------ | ------------ |
|  username | string User.username |
|  email  | string User.email  |
| password  | string User.password   |

**4. POST - /admin_auth**

It verifies the identity of the admin.  It gives the admin the authority to use the service.

**Request**

| Param  | Value  |
| ------------ | ------------ |
| admin  | string Admin.admin   |
| admin_pass  | string Admin.admin_password   |


**5.  GET -  /admin_auth**

It terminates the admin's authority to access the service.

**6. GET - /books**

Gets all the books

**Response**

| Params |
| ------------ |
| title   |
|  author |
|  type |
|  barcode |
|  status |
|  imgname |

**7.  POST -  /book_add**

Adds new books to database

**Request**

|  Params | Value  |
| ------------ | ------------ |
| title  | string Book.title   |
| author   | string Book.author   |
| type   | string Type.ID   |
|  barcode | string Book.barcode   |
| pic  | file  |


**8. GET -  /borrow_book/{id}**

Adds the relevant book to the borrowed table.

**Request**

|  Params | Value   |
| ------------ | ------------ |
| {id}  | int Book.ID  |

**9. GET -  /postpone/{id}**

It updates the delivery date of the relevant book.

**Request**

|  Params | Value   |
| ------------ | ------------ |
| {id}  | int Book.ID  |

**10. GET -  /delivery_book/{id}**

Deletes the relevant book from the borrowed table

**Request**

|  Params | Value   |
| ------------ | ------------ |
| {id}  | int Book.ID  |

**11. GET -  /book_delete/{id}**

Deletes the relevant book from the book table.

**Request**

|  Params | Value   |
| ------------ | ------------ |
| {id}  | int Book.ID  |

**12. GET - /user_delete/{id}**

Deletes the relevant user from the user table.

**Request**

|  Params | Value   |
| ------------ | ------------ |
| {id}  | int User.ID  |

**13.  POST - /update_name**

Updates the user's username

**Request**

|  Params |  Value |
| ------------ | ------------ |
|  username | string User.username  |


**14. POST - /change_pass**

Updates the user's password

**Request**

|  Params |  Value |
| ------------ | ------------ |
|  password | string User.password  |

**15. POST - /admin_book_search**

Searches by title, author or barcode from the book table according to request and returns matching data for admin.

**16. POST - /member_search**

Searches by username from the user's table according to request and returns matching data for admin.

**17. POST - /book_search**

Searches by title, author or barcode from the book table according to request and returns matching data for user.

**18. GET -/getInfo/{id}**

Matches the related book with the borrow table and the user table using ID.

**Request**

|  Params | Value   |
| ------------ | ------------ |
| {id}  | int Book.ID |






































