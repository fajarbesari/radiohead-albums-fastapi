from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Radiohead Albums API")

class Album(BaseModel):
    title: str
    year: int
    label: str
    cover_url: str

# Mount static folder
app.mount("/static", StaticFiles(directory="static"), name="static")
# Static dataset of Radiohead albums

baseUrl = "127.0.0.1:8000"


albums_data = [
    Album(
        title="Pablo Honey",
        year=1993,
        label="Parlophone",
        cover_url= f"{baseUrl}/static/albums/pablo.jpg"
    ),
    Album(
        title="The Bends",
        year=1995,
        label="Parlophone",
        cover_url=f"{baseUrl}/static/albums/thebends.jpg"
    ),
    Album(
        title="OK Computer",
        year=1997,
        label="Parlophone",
        cover_url=f"{baseUrl}/static/albums/okcomputer.png"
    ),
    Album(
        title="Kid A",
        year=2000,
        label="Parlophone",
        cover_url=f"{baseUrl}/static/albums/kida.jpg"
    ),
    
    Album(
        title="Amnesiac",
        year=2001,
        label="Parlophone",
        cover_url=f"{baseUrl}/static/albums/amnesiac.jpg"
    ),
    Album(
        title="Hail to the Thief",
        year=2003,
        label="Parlophone",
        cover_url=f"{baseUrl}/static/albums/hailtothethief.jpg"
    ),
    Album(
        title="In Rainbows",
        year=2007,
        label="Self-released",
        cover_url=f"{baseUrl}/static/albums/inrainbows.jpg"
    ),
    Album(
        title="The King of Limbs",
        year=2011,
        label="XL Recordings",
        cover_url=f"{baseUrl}/static/albums/thekingofthelimbs.jpg"
    ),
    Album(
        title="A Moon Shaped Pool",
        year=2016,
        label="XL Recordings",
        cover_url=f"{baseUrl}/static/albums/amoonshapedpool.jpg"
    ),
]

@app.get("/albums", response_model=List[Album])
def get_albums():
    return albums_data
