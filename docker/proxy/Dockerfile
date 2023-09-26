FROM nginx
EXPOSE 80
EXPOSE 443

#ARG JAR_FILE=*.jar
COPY dist/*.conf /etc/nginx/conf.d
#COPY build/ /app/
#COPY dist/* /etc/rabbitmq/
#ENTRYPOINT ["java","-jar","/app.jar"]

#ADD ./demo-0.0.1-SNAPSHOT.jar app.jar
#ENTRYPOINT ["java" , "-jar", "app.jar"]
#CMD mkdir /etc/letsencrypt
#RUN mkdir /etc/letsencrypt
# 앱 디렉터리 생성
#WORKDIR /app
# 앱 의존성 설치
# 가능한 경우(npm@5+) package.json과 package-lock.json을 모두 복사하기 위해
# 와일드카드를 사용
#COPY package*.json ./
#COPY . .
#RUN npm install

#COPY index-http.js ./
#CMD ["node","index-http.js"]

