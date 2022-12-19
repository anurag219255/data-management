FROM python:3.8

# Install OS Modules
RUN apt update -y && \
     apt install telnet -y && \
     rm -rf /var/lib/apt/lists/*

# Copy source code # It is used to copy data source files into the image
RUN mkdir -p /data-management
COPY app /data-management/app
COPY requirements.txt /data-management

#Install application dependencies
RUN pip install -r /data-management/requirements.txt