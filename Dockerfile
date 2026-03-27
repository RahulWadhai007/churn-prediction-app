# Use the slim version of Python 3.11 to keep the base image small
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# COPY requirements FIRST to leverage Docker layer caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy EVERYTHING in your current folder (app.py, model, and scaler) into /app
COPY . . 

# Expose the port Streamlit runs on
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]