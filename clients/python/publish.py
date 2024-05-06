import pika
import sys

rabbitmq_host = (
    "localhost"  # Change this if your RabbitMQ server is on a different host
)
rabbitmq_port = 8081  # Default RabbitMQ port
rabbitmq_queue = "tyk"
rabbitmq_user = "ataimo@tyk.io"
rabbitmq_password = "alex1234."

credentials = pika.PlainCredentials(username=rabbitmq_user, password=rabbitmq_password)
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host=rabbitmq_host, port=rabbitmq_port, credentials=credentials
    )
)
channel = connection.channel()

channel.queue_declare(queue=rabbitmq_queue, durable=True)

message = " ".join(sys.argv[1:]) or "info: Hello, RabbitMQ!"

channel.basic_publish(
    exchange="",
    routing_key=rabbitmq_queue,
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=2,  # Make the message persistent
    ),
)

print(f" [x] Sent '{message}'")

connection.close()
