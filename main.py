from fastapi import FastAPI
from agents.controller import Controller

app = FastAPI()
controller = Controller()

@app.get("/query")
async def query(q: str):
    response = controller.process_query(q)
    return {"response": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)