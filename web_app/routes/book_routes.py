# web_app/routes/book_routes.py

from flask import Blueprint, jsonify, request, render_template #, flash, redirect
from web_app.models import db, Book, parse_records

book_routes = Blueprint("book_routes", __name__)

@book_routes.route("/books.json")
def list_books():
#     books = [
#         {"id": 1, "title": "Book 1"},
#         {"id": 2, "title": "Book 2"},
#         {"id": 3, "title": "Book 3"},
#     ]
    # SELECT * FROM books
    book_records = Book.query.all()
    print(book_records)
    books = parse_records(book_records) # parse_records to convert the book_records into dictionaries
    return jsonify(books)

@book_routes.route("/books")
def list_books_for_humans():
#     books = [
#         {"id": 1, "title": "Book 1"},
#         {"id": 2, "title": "Book 2"},
#         {"id": 3, "title": "Book 3"},
#     ]
    # SELECT * FROM books
    book_records = Book.query.all()
    print(book_records)
    books = parse_records(book_records) # parse_records to convert the book_records into dictionaries
    return render_template("books.html", message="Here's some books", books=books)

@book_routes.route("/books/new")
def new_book():
    return render_template("new_book.html")

@book_routes.route("/books/create", methods=["POST"]) # we can also use methods=["GET", "POST"]

def create_book():
    print("FORM DATA:", dict(request.form))

    # todo: store in database
    # INSERT INTO books ...

    # Intinialize new_book object, which is an instance of the class Book 
    new_book = Book(title=request.form["title"], author_id=request.form["author_name"])
    db.session.add(new_book)
    db.session.commit()


    return jsonify({
        "message": "BOOK CREATED OK (TODO)",
        "book": dict(request.form)
    })
    #flash(f"Book '{new_book.title}' created successfully!", "success")
    #return redirect(f"/books")