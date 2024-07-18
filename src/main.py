from fastapi import FastAPI
from strawberry.asgi import GraphQL

from gql.schema import schema

app = FastAPI()


@app.get("/")
async def index():
    return {"message": "Welcome to API"}


app.add_route("/graphql", GraphQL(schema))
