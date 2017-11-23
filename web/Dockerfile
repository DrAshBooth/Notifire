# Use an official Python runtime as a parent type
FROM python:3.6

# Set the working directory to /code
WORKDIR /code

# Copy the current directory contents into the container at /code
ADD . /code

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 5050 available to the world outside this container
EXPOSE 5050

# Define environment variable
ENV NAME World

ENV PATH=$PATH:/notifire_web
ENV PYTHONPATH /notifire_web

# Run app.py when the container launches
CMD ["python", "./notifire_web/app.py"]