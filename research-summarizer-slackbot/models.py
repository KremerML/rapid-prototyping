from pydantic import BaseModel


class Paper(BaseModel):
    link: str
    title: str
    summary: str
    channel: str
    shared_by: str
