from app.schemas.graphql.queries import Query
import strawberry

schema = strawberry.Schema(query=Query)
