from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.database import get_db_connection, initialize_db

app = FastAPI(title="Pace PR Demo API")

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

@app.on_event("startup")
def startup_event() -> None:
    initialize_db()

@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Welcome to the Clean API"}

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int) -> dict:
    with get_db_connection() as conn:
        cursor = conn.execute("SELECT id, name, email FROM users WHERE id = ?", (user_id,))
        user = cursor.fetchone()
        
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
        
    return dict(user)
