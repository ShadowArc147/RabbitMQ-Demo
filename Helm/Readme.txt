
Python script and RabbitMQ.

This Helm chart deploys two separate Kubernetes deployments, one for RabbitMQ and another for the Python script container. The RabbitMQ deployment runs the official RabbitMQ Docker image, while the Python script deployment runs your custom Python script Docker image.

The rabbitmq container is configured with two ports exposed: 5672 for AMQP traffic, and 15672 for the RabbitMQ management console. The container is also configured with default login credentials (guest/guest) via environment variables.

The python-script container is configured with a single port (port 80) exposed, and environment variables are used to specify the hostname and port of the RabbitMQ server (rabbitmq:5672 in this case).

Note that the two containers are deployed to the same namespace (rabbitmq-python), which means they will be running on the same network by default. This allows them to communicate with each other over the network without the need for any special networking configuration.
