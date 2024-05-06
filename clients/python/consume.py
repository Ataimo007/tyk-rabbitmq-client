import pika

# Connection parameters
rabbitmq_host = 'localhost'  # Change this if your RabbitMQ server is on a different host
rabbitmq_port = 8081         # Default RabbitMQ port
rabbitmq_queue = 'tyk'
rabbitmq_user = "ataimo@tyk.io"
rabbitmq_password = "alex1234."

# Callback function to process incoming messages
def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

# Create a connection to RabbitMQ server
# connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host, port=rabbitmq_port))

credentials = pika.PlainCredentials(username=rabbitmq_user, password=rabbitmq_password)
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host=rabbitmq_host, port=rabbitmq_port, credentials=credentials
    )
)
channel = connection.channel()

# Declare the queue (make sure it exists)
channel.queue_declare(queue=rabbitmq_queue, durable=True)

# Set up the consumer and start listening for messages
channel.basic_consume(queue=rabbitmq_queue, on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
