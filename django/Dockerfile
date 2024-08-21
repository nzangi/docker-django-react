# Use the official Python image with Alpine Linux as the base
FROM python:3.8-alpine

# Set environment variable to prevent Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container to /django
WORKDIR /django

# Copy the requirements file first to leverage Docker cache
COPY requirements.txt /django/requirements.txt
COPY entrypoint.sh /django/entrypoint.sh

# Install dependencies from requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . /django

# Ensure the entrypoint script is executable
RUN chmod +x /django/entrypoint.sh

# Expose port 8000 for the Gunicorn server
EXPOSE 8000

# Set the entrypoint to run the entrypoint.sh script
ENTRYPOINT ["/django/entrypoint.sh"]
