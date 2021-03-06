import strawberry


# Schema type
@strawberry.type
class Book:
    title: str
    author: str


@strawberry.type
class Author:
    name: str


@strawberry.type
class User:
    username: str
    password: str


@strawberry.type
class LoginSuccess:
    username: str
    token: str


@strawberry.type
class LoginError:
    message: str
