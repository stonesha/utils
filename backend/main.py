from typing import Optional
from fastapi import FastAPI
from bs4 import BeautifulSoup
import requests
from pydantic import BaseModel
from requests_html import AsyncHTMLSession
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "http://localhost:3000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class VideoUrlItem(BaseModel):
    url: str
    iframe: bool


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/extract_video/")
async def extract_video(videoUrl: VideoUrlItem):
    session = AsyncHTMLSession()
    response = await session.get(videoUrl.url)
    await response.html.arender(timeout=30)

    video_media_urls = []

    videos = response.html.find(selector='video')

    for video in videos:
        try:
            video_media_urls.append(video.attrs['src'])
        except KeyError:
            sources = video.find('source')
            for source in sources:
                video_media_urls.append(source.attrs['src'])

    if videoUrl.iframe:
        iframes = response.html.find(selector='iframe')
        for iframe in iframes:
            video_media_urls.append(iframe.attrs['src'])

    return video_media_urls
