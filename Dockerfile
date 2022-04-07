#docker build -t rc-falco .
# install base
FROM python:3

# copy the folder to the container:
ADD . /rc-falco

# Define working directory:
WORKDIR /rc-falco

# Install the requirements
RUN pip3 install -r /rc-falco/requirements.txt

# expose tcp port 5000
#EXPOSE 5000

# default command: run the web server
CMD ["python3","app.py"]
