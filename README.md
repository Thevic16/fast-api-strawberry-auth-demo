#  FastAPI Strawberry authentication demo.

The aim of this demo project is to show how to integrate fastAPI 
(Web framework) and strawberry (GraphQL library) to work together
with JWT (JSON Web Token) to authenticate and give permission (using
HTTP Auth headers) to the users to modify the data related to books
and authors schema.

# How this project is organized?

- Configuration package: Here are loaded all the environment variables from
  the .env (read the next section for more info).

- Dataset package: Here are saved the data of the program. Everything is
  saved in memory to keep simple. 

- Schemas package: Here are objects, inputs, queries, and mutations strawberry
  schemas types. 

- Security package: In this package are the functions related to authentication
  of the users, JWT token creation and verification, and class permission that
  uses the previous mention function to authenticate the user. 

- Postman collection folder: Probably you will need an API platform to test
  this project (because you should be able to add the Bearer Token to the
  request) if you don't know one, I recommend you look for Postman which
  includes incredible functionalities like collections (you can add and test
  my premade request). For that reason, I left my collection in this folder. 

# Instruction to run the app.

- First, you have to specify the environment variables creating your .env file
  (see .env-example).
- Second, you have to activate the virtual environment by running 
  'pipenv shell' command.
- Third, you should install all the necessary libraries for the project by 
  running 'pipenv install' command.
- And then you can proceed to run the application by executing the next
  command 'uvicorn main:app'.

# Explanation.

If you try to add an author or a book you will realize that you are not
authorized to perform this action. For this reason, you have to first
create a user with the add user mutation, subsequently, you can use the
login mutation with your credentials to obtain the token. Finally, you are
able to add your token to the auth header of your request and gain access to
the resources that you didn't have in the first place.
