FROM python:3.12-slim

RUN apt-get update && apt-get install -y poppler-utils && apt-get clean

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 80

CMD ["streamlit", "run", "app.py", "--server.port", "80", "--server.address", "0.0.0.0"]
