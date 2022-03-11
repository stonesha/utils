from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/extract_video/{url}")
def read_item(url: str, q: Optional[str] = None):
    return {"url": url, "q": q}
