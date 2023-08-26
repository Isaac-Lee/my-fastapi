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

@app.get("/{name}")
async def name1():
    return "hello {name}"
    

@app.get("/name2")
async def Lim():
    return {"message": "Lim"}
