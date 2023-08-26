from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root(name: str = None):
    if name:
        return {"message": f"Hello World and Hello {name}"}
    return {"message": f"Hello World"}

@app.get("/health")
async def health():
    return {"message": "health"}

@app.get("/name1")
async def name1():
    pass

@app.get("/name2")
async def name2():
    pass
