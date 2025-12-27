# Dockerfile – multi-stage build keeps final image small
FROM python:3.11-slim

# 1. create non-root user
RUN groupadd -r botuser && useradd -r -g botuser botuser

# 2. install dependencies
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 3. copy source
COPY main.py .

# 4. switch to non-root
RUN chown -R botuser:botuser /app
USER botuser

# 5. default command (token must be passed via env)
CMD ["python", "main.py"]
