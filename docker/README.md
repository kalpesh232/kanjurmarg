1. Add a .dockerignore
2. Create a production-ready Dockerfile
3. docker build -t student-performance:1.0 .
4. docker run --rm -p 5000:5000 student-performance:1.0 *
5. docker run -d --name student-app -p 5000:5000 student-performance:1.0
6. docker logs -f student-app *
7. Develop docker-compose.yml *
8. docker compose up --build
8. docker run -v C:\Users\kalpe\kanjurmarg\docker/uploads:/app/uploads -p 5000:5000 student-performance:1.0
9. docker ps / >docker ps -a
   docker logs -f student-app
   docker exec -it student-app/bin/bash
   docker rmi student-performance:1.0
   docker rm <container_id>