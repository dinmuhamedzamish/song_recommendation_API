from fastapi import FastAPI
from api.routes import router

# 1. Create the FastAPI app
app = FastAPI(
    title="Song Recommendation API",
    description="Content-based song recommendation engine",
    version="1.0.0"
)

# 2. Connect your routes from api/routes.py
app.include_router(router, prefix="/api", tags=["Recommendations"])


# 3. Simple welcome message when visiting http://127.0.0.1:8000/
@app.get("/")
def root():
    return {"message": "Song Recommendation API is live! Go to /docs to test it."}
