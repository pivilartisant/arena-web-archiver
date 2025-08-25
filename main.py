from typing import Union
from datetime import datetime
from pydantic import BaseModel
from fastapi import FastAPI,HTTPException
import requests
import json
import subprocess
import re


app = FastAPI()

base_url = "https://api.are.na/v2"

# return archived in tmp
@app.get("/")
async def root():
    return {"Hello": "World"}

@app.get("/archive/")
async def get_url_from_block(block_url:str, archive_method:str):
    headers = {
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0 (compatible; FastAPI-Client/1.0)"
}
    # parse the url
    url = parse_arena_url(block_url)
    r = requests.get(url, headers=headers)
    if r.status_code == requests.codes.ok:
        print("Reponse OK :3")
    else:
        r.raise_for_status()
    ## todo: return url and recomposed title for warcfile
    if archive_method == "snapshot":
        print(f"making snapshot of {block_url}")
    elif archive_method == "mirror":
          print(f"mirroring {block_url}")
    else:
        raise HTTPException(status_code=403, detail="Archiving method not found")
    
    return r.json().get('source').get('url')

    #website_url = r.json().get('source').get('url')
    #return {status: "Website archived thank you for your service o7"}


def parse_arena_url(block_url:str):
    block_id = re.findall('[0-9]+', block_url)
    return f"{base_url}/blocks/{''.join(block_id)}"

def archive_url(url: str, warc_file_name: str):
    cmd = [
        "wget",
        "--mirror",                 
        "--convert-links",          
        "--page-requisites",         
        "--no-parent",              
        f"--warc-file={warc_file_name}", 
        url
    ]
    subprocess.run(cmd, check=True)

def snapshot_url(url: str, warc_file_name: str):
    cmd = [
        "wget",
        url
    ]
    subprocess.run(cmd, check=True)
