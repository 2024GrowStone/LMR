from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LoginData(BaseModel):
    username: str
    password: str

@app.post("/login")
async def login(data: LoginData):
    """
    login check
    """
    if data.username == "test" and data.password == "1234":
        return { 
            "agent": "Kim MinSup",
            "success": True 
        }
    else:
        raise HTTPException(status_code=400, detail="Invalid credentials")


@app.post("/get_eval")
async def get_eval():
    pass