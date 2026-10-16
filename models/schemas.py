from typing import Optional
from sqlmodel import Field, SQLModel

class Song(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    artists: str
    track_name: str
    tempo: float
    energy: float
    loudness: float

















