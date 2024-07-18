import strawberry


@strawberry.type
class Project:
    id: int
    name: str
    description: str


@strawberry.input
class ProjectInput:
    name: str
    description: str

