from pydantic import BaseModel


class TodoEntrySchema(BaseModel):
    id: str
    content: str
    tags: list[str]

class TodoEntryAddSchema(BaseModel):
    content: str
