from fastapi import APIRouter, HTTPException
from core.recommender import recommend_by_song_name

router = APIRouter()

@router.get("/recommend")
def get_recommendations(song_name: str, top_k: int = 5):
    result = recommend_by_song_name(track_name=song_name, top_k=top_k)
    
    if not result.get("found"):
        raise HTTPException(status_code=404, detail=result.get("message"))
        
    return result
