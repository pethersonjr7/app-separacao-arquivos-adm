# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 3000 available to the world outside this container (documentation)
EXPOSE 8080

# Run gunicorn when the container launches, binding to the $PORT environment variable
# Cloud Run sets this variable automatically. Default to 8080 if not set.
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:${PORT:-8080} --timeout 900 app:app"]
