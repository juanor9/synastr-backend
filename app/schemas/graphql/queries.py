import strawberry
from typing import List, Optional
from app.database.mongo_client import users_collection

@strawberry.type
class User:
    email: str
    username: str
    created_at: Optional[str]

@strawberry.type
class Query:
    @strawberry.field
    def users(self) -> List[User]:
        users = list(users_collection.find({}, {"_id": 0}))  # Excluir _id
        return [User(**user) for user in users]
