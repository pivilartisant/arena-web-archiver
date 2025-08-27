server:
	uv run fastapi dev
docker-build:
	docker build -t arena-web-archiver .   
docker-run:
	docker run -p 8000:8000 arena-web-archiver