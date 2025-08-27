# arena-web-archiver

This minimal and selfhosted utiliy for Are.na is built with <a href="https://htmx.org/">HTMX</a>, <a href="https://fastapi.tiangolo.com/">FastAPI</a> and <a href="https://www.gnu.org/software/wget/">WGET</a>.

<div>
Some Details:
</div>
<ul>
<li>Website archived will be save as HTML and WARC files.</li>
<li>If no WARC filename is given are.na block id will be used.</li>
<li>Archives are saved in the **/tmp/arena_archives** directory on your filesystem when using docker. If not, they'll be savec in the **/tmp** directory directly in the project repo.</li>
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
