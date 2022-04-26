from function import get_greater_roman

import strawberry
from strawberry.fastapi import GraphQLRouter
from typing import Optional


@strawberry.type
class Response:
    number: Optional[str] = None
    value: Optional[int] = None


@strawberry.type
class Mutation:
    @strawberry.mutation
    def search(text: str) -> Response:
        response = get_greater_roman(text)
        return Response(
            number=response.get("number"),
            value=response.get("value")
        )


schema = strawberry.Schema(query=Response, mutation=Mutation)
router = GraphQLRouter(schema)