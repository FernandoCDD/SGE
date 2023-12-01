FROM debian:bookworm-slim
RUN apt-get update && apt-get install -y apache2 libapache2-mod-php php7.3 && \
apt-get clean && \
rm -rf /var/lib/apt/lists/*

RUN rm /var/www/html/index.html
COPY src /var/www/html

EXPOSE 80
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]