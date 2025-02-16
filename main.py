from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.post("/run")
async def run_task(task: str):
    if not task:
        raise HTTPException(status_code=400, detail="Task description required.")
    return {"message": f"Executing task: {task}"}

@app.get("/read")
async def read_file(path: str):
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        return {"content": content}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
