from pydantic import BaseModel, Field


class TreesRequestBody(BaseModel):
    country: str
    city: str
    year: int = Field(ge=2013)
