# Base image
FROM python:2.7
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set the working directory in the container
WORKDIR /app
# Copy the requirements file
COPY requirements.txt .
# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y supervisor nginx
# Copy the project code into the container
COPY . .
COPY ./compose/supervisor/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
# Expose the port for the Django development server
EXPOSE 8000
# Start the Django development server
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]