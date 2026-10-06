# base image
FROM python:3.9-slim

# set working directory
WORKDIR /app

# copy all files from local to container
COPY . . 


# Start the application
CMD ["python","number_guessing_game.py"]