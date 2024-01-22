# Get python Image to exec the script
FROM python:3.10.13-alpine3.19

# Copy the app directory to the container
ADD app /app

# change directory to app
WORKDIR /app

# install python modules
RUN pip install -r requirement.txt

# exec the script
CMD ["sh", "-c", "python main.py"]