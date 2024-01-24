# Get python Image to exec the script
FROM python:3.10.13-alpine3.19

# Install libxml2 and libxslt development packages
RUN apk add --no-cache libxml2-dev libxslt-dev

# Install build dependencies for lxml
RUN apk add --no-cache build-base

# Install ninja as a system package
RUN apk add --no-cache ninja

# Copy the app directory to the container
ADD app /app

# Change directory to app
WORKDIR /app

# Install python modules
RUN pip install -r requirement.txt

# Exec the script
CMD ["python", "main.py"]
