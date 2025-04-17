FROM python:3.10

WORKDIR /app

COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install flask flask_cors


COPY . .
EXPOSE 5001
CMD ["python", "app.py"]
