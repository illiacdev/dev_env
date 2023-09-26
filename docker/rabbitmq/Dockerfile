FROM rabbitmq:3-management
ENV RABBITMQ_DEFAULT_USER user
ENV RABBITMQ_DEFAULT_PASS "0000"
#RUN rabbitmq-plugins enable --offline rabbitmq_mqtt rabbitmq_federation_management rabbitmq_stomp
#RUN rabbitmq-plugins enable --offline rabbitmq_mqtt rabbitmq_federation_management
RUN rabbitmq-plugins enable --offline rabbitmq_mqtt rabbitmq_web_mqtt
