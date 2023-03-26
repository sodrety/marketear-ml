FROM python:3.9
#FROM python:3.10
RUN apt-get update
RUN apt-get  install -y  libgirepository1.0-dev
#RUN apt update && \
#    apt-get install -y openjdk-11-jdk && \
#    apt-get install -y ant && \
#    apt-get clean;

# Set JAVA_HOME
#ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64/
#RUN export JAVA_HOME

COPY . /app
WORKDIR /app
#RUN pip3 --version
RUN python -m pip install --upgrade pip

RUN pip install mysql-connector-python
RUN pip install cython
RUN pip install pyjnius
RUN pip install pickle5
RUN pip install pygobject PyGObject
#RUN pip install truststore

RUN python --version
RUN pip install -r requirements.txt
CMD [ "python", "app.py"] 
