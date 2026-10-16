import numpy as np
from models.schemas import Song
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from core.recommender import extract_features
def test_extract_features():
    # 1. Arrange: Create a mock song 🎵
    sample_song = Song(
        id=1,
        track_name="Test Song",
        artists="Test Artist",
        tempo=120.0,
        energy=0.8,
        loudness=-5.0,
    )

    # 2. Act: Run the feature extractor ⚙️
    result = extract_features([sample_song])

    # 3. Assert: Verify the output guarantees expected behavior 🔍
    assert result["song_ids"] == [1]
    assert result["matrix"].shape == (1, 3)