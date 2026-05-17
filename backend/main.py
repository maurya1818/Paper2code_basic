from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.router import router
from database import engine, Base

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Paper2Code API")

# Configure CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # For MVP, allow all. In production, specify origins.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to Paper2Code API"}
