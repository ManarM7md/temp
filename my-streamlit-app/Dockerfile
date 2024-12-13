FROM python:3.12-slim

# Install Poppler utilities
RUN apt-get update && apt-get install -y poppler-utils

# Set the working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Command to run the app
CMD ["streamlit", "run", "app.py", "--server.port", "80", "--server.address", "0.0.0.0"]
