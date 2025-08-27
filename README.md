# arena-web-archiver

## How to use 
1) Clone repo
2) Have python and and UV package manager installed on your machine
3) ```uv sync```
4) ```source .venv/bin/activate```
5) Start the server using ```make server``` ((don't forget to activiate the venv))
6) Access on http://127.0.0.1:8000
7) See docs at http://127.0.0.1:8000/docs

flow: save a block -> get block url -> send block to service (api or client) -> get archiving confirmation