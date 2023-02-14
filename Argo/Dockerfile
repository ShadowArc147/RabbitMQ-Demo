FROM rabbitmq:latest 

# Enable RabbitMQ Management plugin
RUN rabbitmq-plugins enable rabbitmq_management 

# Expose the necessary ports
EXPOSE 5672 15672 

# Set the default user and password for the management console
ENV RABBITMQ_DEFAULT_USER=user
ENV RABBITMQ_DEFAULT_PASS=password
