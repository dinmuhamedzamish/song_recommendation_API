from typing import List, Optional
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler

from models.schemas import Song
from data.data_fetching import fetch_songs


def extract_features(songs: List[Song]) -> dict:
    if not songs:
        raise ValueError("No songs provided")
    song_ids = [song.id for song in songs]
    feature_matrix = np.array([
        [song.tempo, song.energy, song.loudness]
        for song in songs
    ])
    scaler = MinMaxScaler()
    scaled_matrix = scaler.fit_transform(feature_matrix)
    return {
        "song_ids": song_ids,
        "matrix": scaled_matrix,
        "scaler": scaler
    }


def recommend_by_song_name(track_name: str, top_k: int = 5) -> dict:
    # 1. Fetch songs from DB
    all_songs = fetch_songs()
    if not all_songs:
        return {"error": "Database is empty."}

    # 2. Search for the song (case-insensitive)
    target_idx = None
    for idx, song in enumerate(all_songs):
        if song.track_name.strip().lower() == track_name.strip().lower():
            target_idx = idx
            break

    # 3. If not found, return a clean message
    if target_idx is None:
        return {
            "found": False,
            "message": f"Song '{track_name}' was not found in the database.",
            "recommendations": []
        }

    # 4. Extract & scale features for all songs
    data = extract_features(all_songs)
    matrix = data["matrix"]

    # 5. Get the target song's vector and compare with all others
    target_vector = matrix[target_idx].reshape(1, -1)
    similarities = cosine_similarity(target_vector, matrix)[0]

    # 6. Sort by highest similarity
    ranked_indices = np.argsort(similarities)[::-1]

    # 7. Exclude the song itself (so you don't recommend the same song!)
    recommended_indices = [
        idx for idx in ranked_indices if idx != target_idx
    ][:top_k]

    return {
        "found": True,
        "target_song": all_songs[target_idx],
        "recommendations": [all_songs[idx] for idx in recommended_indices]
    }
