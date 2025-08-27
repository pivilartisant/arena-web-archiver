# arena-web-archiver

## How to use 
1) Clone repo
2) Have Python and and UV package manager and WGET installed on your machine
5) Start the server using ```make server``` 
6) Access on http://127.0.0.1:8000
7) See docs at http://127.0.0.1:8000/docs

## with docker (don't use it yet)
1) run ```make docker-build```
2) run ```make docker-run```
3) Access on http://127.0.0.1:8000
4) See docs at http://127.0.0.1:8000/docs

### contribute
See https://github.com/pivilartisant/arena-web-archiver/issues 

  This minimal and selfhosted utiliy for Are.na is built with <a href="https://htmx.org/">HTMX</a>, <a href="https://fastapi.tiangolo.com/">FastAPI</a> and <a href="https://www.gnu.org/software/wget/">WGET</a>.

<div>
Some Details:
</div>
<ul>
<li>Website archived will be save as HTML and WARC files.</li>
<li>If no WARC filename is given are.na block id will be used.</li>
<li>Archive are saved in the /tmp directory in the project (not the global /tmp in your filesystem).</li>
<li><em>Mirror</em> makes a 1:1 copy of the website. <em>Snapshot</em> only archives a single page.</li>
</ul>

<div>
  Recommendations:
</div>
<ul>
  <li>Use this tool to save oldweb things that may disapear one day.</li>
  <li>It's not super complex or anything, so expect the bare minimum.</li>
  <li>While mirroring some website will create an infinte loop, this error is not handled.</li>
  <li>For large websites and archives, it's probably better to not use this tool.</li>
</ul>
<div>