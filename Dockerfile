FROM python:3.7

WORKDIR /app

# Copy the current directory (.), into a container in /app
COPY app /app

EXPOSE 80