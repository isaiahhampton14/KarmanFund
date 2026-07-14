from fastapi import FastAPI

app = FastAPI(
    title="KarmanFund API",
    version="0.1.0"
)

@app.get("/")
async def root():
    return {
        "message": "Welcome to KarmanFund",
        "status": "running"
    }