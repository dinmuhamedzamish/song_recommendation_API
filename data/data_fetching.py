from pathlib import Path
from sqlmodel import Session, SQLModel, create_engine, select
from models.schemas import Song

# Always resolve the exact folder where this file lives:
DB_PATH = (Path(__file__).resolve().parent / "song_db.db").as_posix()

engine = create_engine(f"sqlite:///{DB_PATH}")

def fetch_songs() -> list[Song]:
    with Session(engine) as session:
        songs = session.exec(select(Song)).all()
        return songs
