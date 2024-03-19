FROM python:3.11.8-alpine3.19

# Copy the source code to the container
COPY models /appfiles/models
COPY migrate.py /appfiles/migrate.py
COPY requirements.txt /appfiles/requirements.txt

# Install the required packages
RUN pip install -r /appfiles/requirements.txt

WORKDIR /app

# Add the command to run the app
ENTRYPOINT ["python", "/appfiles/migrate.py"]
