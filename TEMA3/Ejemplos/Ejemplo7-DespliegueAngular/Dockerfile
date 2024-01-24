FROM node as build
WORKDIR /app/
COPY ./package.json /app/
RUN npm install
COPY ./ /app/
RUN npm run buildProd

FROM nginx 

COPY ./nginx.conf /etc/nginx/nginx.conf

RUN rm -rf /usr/share/nginx/html/*

COPY --from=build /app/dist/HelloWorld /usr/share/nginx/html




