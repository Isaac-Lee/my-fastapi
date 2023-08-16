from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root(name: str = None):
    if name:
        return {"message": f"Hello World and Hello {name}"}
    return {"message": f"Hello World"}

@app.get("/health")
async def health():
    return {"message": "healthy"}