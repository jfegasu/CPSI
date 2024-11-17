FROM python:3.12-slim

WORKDIR /app
COPY requi.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requi.txt

COPY . .
CMD [ "python3","app.py"]



