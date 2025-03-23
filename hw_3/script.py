import csv
import json
from pydantic import BaseModel, Field
from typing import List, Iterator


class BookModel(BaseModel):
    title: str = Field(alias="Title")
    author: str = Field(alias="Author")
    pages: int = Field(alias="Pages")
    genre: str = Field(alias="Genre")


class UserModel(BaseModel):
    name: str
    gender: str
    address: str
    age: int
    books: List[BookModel] = []


def load_books(filename: str):
    with open(filename, newline="") as file:
        return [BookModel(**book) for book in csv.DictReader(file)]


def load_users(filename: str):
    with open(filename) as file:
        users = json.load(file)
        return [UserModel(**{key: user[key] for key in ["name", "gender", "address", "age"]}) for user in users]


def books_for_users(users: List[UserModel], books: List[BookModel]):
    min_books = len(books) // len(users)
    extra_books = len(books) % len(users)

    book_iterator = iter(books)

    for i, user in enumerate(users):
        extra = 1 if i < extra_books else 0
        user.books = [next(book_iterator) for i in range(min_books + extra)]

    return users


def save_result(filename: str, users: List[UserModel]):
    with open(filename, 'w') as file:
        json.dump([user.dict(by_alias=True) for user in users], file, indent=4)


# Основная логика
books = load_books("books.csv")
users = load_users("user.json")
users_with_books = books_for_users(users, books)
save_result("result.json", users_with_books)
