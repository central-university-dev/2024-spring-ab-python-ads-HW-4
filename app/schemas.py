"""All schemas."""

from pydantic import BaseModel


class InputFeatures(BaseModel):
    """Input features."""

    city: str = ""
    country: str = ""
    year: str = ""
