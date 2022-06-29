import strawberry

from schemas.mutations import Mutation
from schemas.queries import Query
from fastapi import FastAPI
from strawberry.asgi import GraphQL

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQL(schema)

app = FastAPI()
app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)
