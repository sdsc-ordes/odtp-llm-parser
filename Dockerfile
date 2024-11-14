FROM ubuntu:22.04

LABEL maintainer="Your Name <your.email@example.com>"
LABEL version="v0.0.1"
LABEL description="ODTP component based on Ubuntu 22.04"
LABEL org.opencontainers.image.title="ODTP Component"
LABEL org.opencontainers.image.vendor="Your Organization"
LABEL org.opencontainers.image.source="https://github.com/your-org/your-repo"
LABEL org.opencontainers.image.licenses="XXX"

##################################################
# Ubuntu setup
##################################################

# Ubuntu setup
RUN apt update && apt install -y \
    python3.10 \
    python3-pip \
    wget \
    unzip \
    nano \
    git \
    g++ \
    gcc \
    htop \
    zip \
    ca-certificates && \
    rm -rf /var/lib/apt/lists/*

##################################################
# ODTP setup
##################################################

COPY odtp-component-client/requirements.txt /tmp/odtp.requirements.txt
RUN pip install -r /tmp/odtp.requirements.txt


#######################################################################
# PLEASE INSTALL HERE ALL SYSTEM DEPENDENCIES RELATED TO YOUR TOOL
#######################################################################

# Installing dependecies from the app
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt


######################################################################
# ODTP COMPONENT CONFIGURATION. 
# DO NOT TOUCH UNLESS YOU KNOW WHAT YOU ARE DOING.
######################################################################

##################################################
# ODTP Preparation
##################################################

RUN mkdir /odtp \
    /odtp/odtp-config \
    /odtp/odtp-app \
    /odtp/odtp-component-client \
    /odtp/odtp-logs \ 
    /odtp/odtp-input \
    /odtp/odtp-workdir \
    /odtp/odtp-output 

# This copy all the information for running the ODTP component
COPY odtp.yml /odtp/odtp-config/odtp.yml

COPY ./odtp-component-client /odtp/odtp-component-client

COPY ./app /odtp/odtp-app
WORKDIR /odtp

# Fix for end of the line issue on Windows. Avoid error when building on windows
RUN find /odtp -type f -iname "*.sh" -exec sed -i 's/\r$//' {} \;

ENTRYPOINT ["bash", "/odtp/odtp-component-client/startup.sh"]