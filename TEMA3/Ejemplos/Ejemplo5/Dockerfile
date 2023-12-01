FROM debian

WORKDIR /app
RUN dpkg -l > lista1.txt
RUN apt update && apt install apache2 -y
RUN dpkg -l > lista2.txt
EXPOSE 80
ENTRYPOINT [ "apache2ctl","-D", "FOREGROUND" ]