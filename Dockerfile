FROM registry.access.redhat.com/ubi8/ubi
RUN yum install -y python3; yum clean all
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN python3 -m pip install -r requirements.txt
COPY ./src /app/src
EXPOSE 7878
ENTRYPOINT ["python3"]
CMD ["src/main.py"]
