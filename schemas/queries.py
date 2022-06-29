import strawberry
import typing

from data.dataset import get_books, get_authors, get_users
from schemas.objects import Book, Author, User


@strawberry.type
class Query:
    books: typing.List[Book] = \
        strawberry.field(resolver=get_books)

    authors: typing.List[Author] = strawberry.field(resolver=get_authors)

    users: typing.List[User] = strawberry.field(resolver=get_users)
