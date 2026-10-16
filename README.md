
# 🎵 Song Recommendation REST API

A content-based music recommendation engine and REST API built with **FastAPI**, **Scikit-Learn**, and **SQLModel**. 

Given a song title, the engine finds the most acoustically similar tracks in the database by analyzing audio features and calculating cosine similarity across normalized multidimensional vectors.

---

## 🚀 Features

- **Content-Based Filtering**: Compares tracks using core Spotify audio characteristics: *tempo*, *energy*, and *loudness*.
- **Feature Scaling**: Implements `MinMaxScaler` so that features with large numerical ranges (like tempo) don't overpower subtle features (like energy).
- **FastAPI Backend**: Fast, asynchronous REST API with automatic interactive OpenAPI / Swagger documentation.
- **ORM & SQLite**: Uses `SQLModel` for schema validation and database management.
- **Automated Tests**: Tested using `pytest`.

---

## 🧠 How the Recommendation Engine Works

```
1. User provides a song name (e.g. "Smooth Operator")
                   ⬇
2. Look up the target song in SQLite database
                   ⬇
3. Extract audio features: [tempo, energy, loudness]
                   ⬇
4. Normalize features using MinMaxScaler: [0, 1] range
                   ⬇
5. Compute Cosine Similarity between target song and all library songs
                   ⬇
6. Rank similarity scores and return the Top-K recommendations
```

---

## 🛠️ Tech Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Server**: [Uvicorn](https://www.uvicorn.org/)
- **Machine Learning**: [Scikit-Learn](https://scikit-learn.org/), [NumPy](https://numpy.org/)
- **Data & Database**: [SQLModel](https://sqlmodel.tiangolo.com/), [Pandas](https://pandas.pydata.org/), [SQLite](https://www.sqlite.org/)
- **Testing**: [Pytest](https://pytest.org/)

---

## 🏁 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/dinmuhamedzamish/song_recommendation_API.git
cd song_recommendation_API
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Seed the Database
Initialize and populate the SQLite database with cleaned song tracks:
```bash
python data/seed_db.py
```

### 4. Run the API Server
```bash
uvicorn main:app --reload
```
The server will start at: `http://127.0.0.1:8000`

---

## 📖 API Documentation

Once the server is running, open your browser to test the interactive Swagger UI:
👉 **http://127.0.0.1:8000/docs**

### Example Request
```http
GET /api/recommend?song_name=Smooth%20Operator&top_k=5
```

### Example Response
```json
{
  "found": true,
  "target_song": {
    "id": 6,
    "artists": "Sade",
    "track_name": "Smooth Operator",
    "tempo": 119.81,
    "energy": 0.559,
    "loudness": -6.491
  },
  "recommendations": [
    {
      "id": 2,
      "artists": "Sade",
      "track_name": "Smooth Operator - Single Version",
      "tempo": 119.336,
      "energy": 0.58,
      "loudness": -6.619
    },
    {
      "id": 7,
      "artists": "Sade",
      "track_name": "Your Love Is King",
      "tempo": 134.624,
      "energy": 0.42,
      "loudness": -6.797
    }
  ]
}
```

---

## 🧪 Running Tests

Run the test suite using `pytest`:
