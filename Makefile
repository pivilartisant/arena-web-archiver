server:
	uv run fastapi dev
docker-create-volume:
	 docker volume create arena_archiver_volume
docker-build:
	docker build -t arena_archiver .   
docker-run:
	docker run --name arena_archiver -v /tmp/arena_archives:/app/tmp/  -p 8000:8000 arena_archiver

