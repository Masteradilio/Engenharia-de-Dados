FROM ubuntu:22.04

# Install python and pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Install boto3
RUN pip3 install boto3

# Set the working directory
WORKDIR /home

# Create a directory for the CSV files
RUN mkdir /home/data

# Set the volume for the CSV files
VOLUME ["/home/data"]

