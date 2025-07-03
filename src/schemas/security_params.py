from pydantic import BaseModel, Field


class Security(BaseModel):
    name: str
    code: str


class SecurityPATCH(BaseModel):
    name: str | None = Field(None)
    code: str | None = Field(None)
