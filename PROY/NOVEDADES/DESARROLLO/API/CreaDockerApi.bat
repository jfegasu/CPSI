docker build --force-rm -t apinovedades . --no-cache
docker run -p 8000:8000 -d --name miapinovedad apinovedades
docker start miapinovedad