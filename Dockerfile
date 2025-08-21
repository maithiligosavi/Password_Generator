# Use a small Python base
FROM python:3.10-slim

WORKDIR /app

# copy requirements if you have one (optional)
# COPY requirements.txt .
# RUN pip install -r requirements.txt

# If no requirements.txt, install Flask
RUN pip install --no-cache-dir flask

COPY . /app

EXPOSE 5000

CMD ["python", "app.py"]
