# Docker Setup for Kryptonite 🐳

This guide explains how to build and run the Kryptonite fire detection API using Docker.

## Prerequisites

- Docker installed on your system
- Docker Compose (usually included with Docker Desktop)

## Quick Start

### Using Docker Compose (Recommended)

1. **Build and start the container:**

   ```bash
   docker-compose up -d
   ```

2. **View logs:**

   ```bash
   docker-compose logs -f
   ```

3. **Stop the container:**
   ```bash
   docker-compose down
   ```

### Using Docker CLI

1. **Build the image:**

   ```bash
   docker build -t kryptonite-api .
   ```

2. **Run the container:**

   ```bash
   docker run -d \
     --name kryptonite-fire-detector \
     -p 8002:8002 \
     --env-file .env \
     -v ./logs:/app/logs \
     -v ./artifact:/app/artifact \
     -v ./config:/app/config:ro \
     kryptonite-api
   ```

3. **View logs:**

   ```bash
   docker logs -f kryptonite-fire-detector
   ```

4. **Stop the container:**
   ```bash
   docker stop kryptonite-fire-detector
   docker rm kryptonite-fire-detector
   ```

## Configuration

### Environment Variables

Create a `.env` file in the project root with your configuration:

```env
# Add your environment variables here
```

### Volume Mounts

The Docker setup includes the following volume mounts:

- `./logs:/app/logs` - Persistent logging
- `./artifact:/app/artifact` - Persistent artifacts
- `./config:/app/config:ro` - Configuration files (read-only)

## Accessing the API

Once the container is running, the API will be available at:

- **Base URL:** `http://localhost:8002`
- **User Routes:** `http://localhost:8002/api/user/*`
- **Map Routes:** `http://localhost:8002/api/map/*`

## Health Check

The container includes a health check that runs every 30 seconds. You can check the container health status with:

```bash
docker ps
```

Look for the `STATUS` column - it should show `healthy` after the container starts.

## Troubleshooting

### Container won't start

1. Check logs:

   ```bash
   docker-compose logs
   ```

2. Verify `.env` file exists and is properly formatted

3. Ensure ports are not already in use:
   ```bash
   netstat -ano | findstr :8002
   ```

### Build fails

1. Clear Docker cache and rebuild:

   ```bash
   docker-compose build --no-cache
   ```

2. Ensure all dependencies in `requirements.txt` are valid

### Permission issues with volumes

On Windows, ensure Docker Desktop has access to the project directory in Settings > Resources > File Sharing.

## Development Mode

For development with hot-reload, you can mount the source code:

```bash
docker run -d \
  --name kryptonite-dev \
  -p 8002:8002 \
  --env-file .env \
  -v ./src:/app/src \
  -v ./logs:/app/logs \
  -v ./artifact:/app/artifact \
  -v ./config:/app/config:ro \
  kryptonite-api \
  uvicorn main:app --host 0.0.0.0 --port 8002 --reload
```

## Production Deployment

For production, consider:

1. Using a reverse proxy (nginx, traefik)
2. Setting up SSL/TLS certificates
3. Configuring proper logging and monitoring
4. Using Docker secrets for sensitive data
5. Setting resource limits in docker-compose.yml

## Updating the Container

1. Pull latest changes
2. Rebuild and restart:
   ```bash
   docker-compose down
   docker-compose up -d --build
   ```
