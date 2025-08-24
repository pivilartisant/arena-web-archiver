from typing import Union
from datetime import datetime
from pydantic import BaseModel
from fastapi import FastAPI
import requests
import json
import subprocess


app = FastAPI()

base_url = "https://api.are.na/v2"

class Block(BaseModel):
    id:int
    title: str | None
    updated_at: datetime
    created_at: datetime
    state: str
    comment_count: int
    generated_title: str
    block_class: str # class is a reveserved word
    base_class: str 
    content: str | None
    content_html: str | None
    description: str | None
    description_html: str | None
    source: dict # hash
    image:  dict
    user: dict
    connections: list

@app.get("/")
async def root():
    return {"Hello": "World"}

@app.get("/get_url/{block}")
async def get_url_from_block(block:str):
    headers = {
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0 (compatible; FastAPI-Client/1.0)"
}
    url = f"{base_url}/blocks/{block}"
 
    r = requests.get(url, headers=headers)
    if r.status_code == requests.codes.ok:
        print("Reponse OK :3")
    else:
        r.raise_for_status()
    ## return url and recomposed title for warcfile
    return r.json().get('source').get('url')


@app.get("/archive_url")
def archive_url(url: str, warc_file_name: str):
    cmd = [
        "wget",
        "--mirror",                  # mirror the site
        "--convert-links",           # convert links for local viewing
        "--page-requisites",         # download CSS, JS, images, etc.
        "--no-parent",               # don’t ascend to parent dirs
        f"--warc-file={warc_file_name}",  # save as WARC
        url
    ]
    subprocess.run(cmd, check=True)

# Example usage:
# archive_url(
#     url="http://www.teleportacia.org/war/",
#     warc_file_name="teleportacia"
# )