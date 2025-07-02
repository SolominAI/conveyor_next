from pydantic import BaseModel, Field


class Security(BaseModel):
    title: str
    name: str


class SecurityPATCH(BaseModel):
    title: str | None = Field(None)
    name: str | None = Field(None)
