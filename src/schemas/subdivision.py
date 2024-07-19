import strawberry


@strawberry.type
class Subdivision:
    id: int
    name: str


@strawberry.input
class SubdivisionInput:
    name: str

