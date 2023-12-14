FROM amazoncorretto:17-alpine
ARG JAR_FILE=target/*.jar
COPY ${JAR_FILE} app.jar
ENTRYPOINT ["java", "-jar","/app.jar"]

#Este Dockerfile iría en el repositorio del proyecto, a la misma altura que el pom.xml