# Use an official Python runtime as a parent type
FROM python:3.6

# Set the working directory to /app
WORKDIR /code

# Copy the current directory contents into the container at /app
ADD . /code

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Run app.py when the container launches
CMD ["python", "initialise_database.py"]