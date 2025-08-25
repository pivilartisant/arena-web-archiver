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
async def archive_website_frim_arena_block(block_url:str, archive_method:str, warc_file_name:str = ""):
    headers = {
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0 (compatible; FastAPI-Client/1.0)"
}
    # parse the url
    req_url, warc_file_name = parse_arena_url(block_url, warc_file_name)
    r = requests.get(req_url, headers=headers)
    item_url = r.json().get('source').get('url')
    if r.status_code == requests.codes.ok:
        print("Reponse OK :3")
    else:
        r.raise_for_status()
    if archive_method == "snapshot":
        print(f"making snapshot of {item_url}")
        process = snapshot_url(item_url, warc_file_name)
        process.check_returncode()
        return {"status": "Website archived thank you for your service o7"}
    elif archive_method == "mirror":
        print(f"mirroring {item_url}")
        process = mirror_url(item_url, warc_file_name)
        process.check_returncode()
        return {"status": "Website archived thank you for your service o7"}
    else:
        raise HTTPException(status_code=403, detail="Archiving method not found")
    



# functions
def parse_arena_url(block_url:str, warc_file_name:str):
    # handle block id parsing
    block_id = re.findall('[0-9]+', block_url)
    url =f"{base_url}/blocks/{''.join(block_id)}"

    # handle filename
    _warc_file_name = ""
    if warc_file_name == "":
        _warc_file_name = block_id
    else :
        _warc_file_name = warc_file_name
    return url, warc_file_name

def mirror_url(url: str, warc_file_name: str):
    cmd = [
        "wget",
        # "--limit-rate=1m"
        "--mirror",                 
        "--convert-links",          
        "--page-requisites",         
        "--no-parent",      
        # "--no-check-certificate"        
        f"--warc-file={warc_file_name}", 
        f"--directory-prefix=./tmp/mirror",
        url
    ]
    return subprocess.run(cmd, check=True)


def snapshot_url(url: str, warc_file_name: str):
    cmd = [
        "wget",
        # "--limit-rate=1m"
        # "--no-check-certificate"
        f"--directory-prefix=./tmp/snapshot",
        url
    ]
    return subprocess.run(cmd, check=True)
