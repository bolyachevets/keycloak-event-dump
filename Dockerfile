FROM google/cloud-sdk:latest

USER root

# Create working directory
RUN mkdir /opt/app-root && chmod 755 /opt/app-root
WORKDIR /opt/app-root

COPY . .

RUN apt-get update && apt-get install -y python3
RUN apt-get update && apt-get install -y python3-pip
RUN python3 -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt

EXPOSE 8080

CMD [ "/bin/bash", "run.sh" ]
