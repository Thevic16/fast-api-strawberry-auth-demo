import os
from datetime import timedelta

import strawberry
from typing import Union

from configuration.enviroment_variables import ACCESS_TOKEN_EXPIRE_MINUTES
from schemas.objects import Book, Author, User, LoginSuccess, LoginError
from data.dataset import books, authors, users
from schemas.inputs import AddBookInput, AddAuthorInput, AddUserInput
from security.authentication import authenticate_user
from security.jwt import create_access_token


@strawberry.type
class Mutation:
    @strawberry.field
    def add_book(self, book: AddBookInput) -> Book:
        new_book = Book(title=book.title, author=book.author)
        books.append(new_book)

        return new_book

    @strawberry.field
    def add_author(self, author: AddAuthorInput) -> Author:
        new_author = Author(name=author.name)
        authors.append(new_author)

        return new_author

    @strawberry.field
    def add_user(self, user: AddUserInput) -> User:
        new_user = User(username=user.username, password=user.password)
        users.append(new_user)

        return new_user

    @strawberry.field
    def login(self, user: AddUserInput) -> Union[LoginSuccess, LoginError]:
        if not authenticate_user(user.username, user.password):
            return LoginError(message="the username or password is not "
                                      "correct")

        # Create token
        access_token_expires = timedelta(
            minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
        access_token = create_access_token(
            data={"sub": user.username}, expires_delta=access_token_expires
        )

        return LoginSuccess(username=user.username, token=access_token)
