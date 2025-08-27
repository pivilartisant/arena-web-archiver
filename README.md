# arena-web-archiver

A minimal, self-hosted utility for [Are.na](https://www.are.na/) built with [HTMX](https://htmx.org/), [FastAPI](https://fastapi.tiangolo.com/), and [Wget](https://www.gnu.org/software/wget/).

---

## Details

- Websites are archived as **HTML** and **WARC** files.  
- If no WARC filename is provided, the Are.na block ID will be used.  
- Archives are saved in:
  - **`/tmp/arena_archives`** when running with Docker.  
  - **`/tmp`** (inside the project repository) when running locally.  
- **Mirror** → creates a 1:1 copy of the entire website.  
- **Snapshot** → archives only a single page.  

---

## Recommendations

- Use this tool to preserve old web content that might disappear one day.  
- It’s intentionally minimal—expect the bare essentials.  
- Some sites may cause infinite loops when mirroring (this error is not currently handled).  
- For very large websites and archives, consider using a more robust archiving tool.  

---



## Get Started
1) Clone repo
2) Have Python and and UV package manager and WGET installed on your machine
5) Start the server using ```make server``` 
6) Access on http://127.0.0.1:8000
7) See docs at http://127.0.0.1:8000/docs

## Get started with docker
1) run ```make docker-create-volume``` 
2) run ```make docker-build```
3) run ```make docker-run```
4) Access on http://127.0.0.1:8000
5) See docs at http://127.0.0.1:8000/docs

### contribute
See https://github.com/pivilartisant/arena-web-archiver/issues 

## License

Shield: [![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg
