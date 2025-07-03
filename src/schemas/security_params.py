from pydantic import BaseModel, Field, ConfigDict


class SecurityAdd(BaseModel):
    name: str
    code: str


class Security(SecurityAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)


class SecurityPATCH(BaseModel):
    name: str | None = Field(None)
    code: str | None = Field(None)
