from pydantic import BaseModel


class TreeCountResponse(BaseModel):
    city: str
    country: str
    year: int
    trees_count: int


class RequestBody(BaseModel):
    city: str
    country: str
    year: int


class MostCityResponse(BaseModel):
    city: str
    count: int
