from fastapi import FastAPI

app = FastAPI()


@app.get("/login")
async def root():
    # 아이디가 존재하는가?
    # 비밀번호가 존재하는 가?
    return { 
            "agent": "Kim MinSup",
            "success": True 
           }
