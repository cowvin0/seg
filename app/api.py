import uvicorn
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from main import app as segs

app = FastAPI()
app.mount("/", WSGIMiddleware(segs.server))

@app.get("/")
def index():
    return "testando"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8050)