from pydantic import BaseModel, HttpUrl

class RequestDto(BaseModel):
    long_url: HttpUrl

class ResponseDto(BaseModel):
    id: int
    short_code: str
    short_url: str
    long_url: str

