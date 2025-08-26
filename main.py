from typing import Union, Literal, Optional
from datetime import datetime
from pydantic import BaseModel
from fastapi import FastAPI,HTTPException, staticfiles, responses,  Request, Form, Query
import requests
import json
import subprocess
import re
import os

app = FastAPI()

base_url = "https://api.are.na/v2"

app.mount("/static", staticfiles.StaticFiles(directory="frontend"), name="static")

class Archive_Repsonse(BaseModel):
   block_url:str
   archive_method:Literal["snapshot", "mirror"]
   warc_file_name:str
   status:str



# Root route
@app.get("/")
async def root():
    return {"hello":"world"}

# Root route
@app.get("/client")
async def root():
    return responses.FileResponse(os.path.join("frontend", "index.html"))


@app.api_route("/archive/", methods=["GET", "POST"], status_code=200)
async def archive_website_from_arena_block(
    request: Request,
    block_url: Optional[str] = Query(None),
    archive_method: Literal["snapshot", "mirror"] = Query("snapshot"),
    warc_file_name: str = Query("")
    ):

    request_method = request.method

    if request_method == "POST" and block_url is None:
        form = await request.form()
        block_url = form.get("block_url")
        archive_method = form.get("archive_method", "snapshot")
        warc_file_name = form.get("warc_file_name", "")

    headers = {
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0 (compatible; FastAPI-Client/1.0)"
    }

    # parse the url
    req_url, warc_file_name = parse_arena_url(block_url, warc_file_name)

    # assert request is okay
    r = requests.get(req_url, headers=headers)
    item_url = r.json().get('source').get('url')
    if r.status_code == requests.codes.ok:
        print("Reponse OK :3")
    else:
        r.raise_for_status()

    # hanlde parsing logic
    if archive_method == "snapshot":
        process = snapshot_url(item_url, warc_file_name)
        process.check_returncode()
        return handle_archive_reponse(request_method,block_url,item_url, archive_method, warc_file_name)
    elif archive_method == "mirror":
        process = mirror_url(item_url, warc_file_name)
        process.check_returncode()
        return handle_archive_reponse(request_method,block_url,item_url, archive_method, warc_file_name)
    else:
        raise HTTPException(status_code=403, detail="Archiving method not found")
    

def handle_archive_reponse(method: Literal["POST", "GET"],block_url:str,item_url:str, archive_method:Literal["snapshot", "mirror"],warc_file_name:str,):
    if method == "POST":
         return  responses.HTMLResponse(
            f"""
            <div>
                Successfully archived {item_url}
            </div>
            """
        )
    else:
        return responses.JSONResponse(Archive_Repsonse(
            block_url=block_url,
            archive_method=archive_method,
            warc_file_name=warc_file_name,
            status="archived"
        ).model_dump())

# functions
def parse_arena_url(block_url:str, warc_file_name:str):
    # handle block id parsing
    block_id = re.findall('[0-9]+', block_url)
    block_id = ''.join(block_id)
    url =f"{base_url}/blocks/{block_id}"

    # handle filename
    _warc_file_name = ""
    if warc_file_name == "":
        _warc_file_name = block_id
    else :
        _warc_file_name = warc_file_name
    return url, _warc_file_name

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
        f"--directory-prefix=./tmp/mirror/{warc_file_name}",
        url
    ]
    return subprocess.run(cmd, check=True)


def snapshot_url(url: str, warc_file_name: str):
    cmd = [
        "wget",
        # "--limit-rate=1m"
        # "--no-check-certificate"
        f"--directory-prefix=./tmp/snapshot/{warc_file_name}",
        url
    ]
    return subprocess.run(cmd, check=True)
