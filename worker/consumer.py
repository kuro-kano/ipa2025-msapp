"""Worker that consumes jobs from RabbitMQ and processes them."""
import os, time, pika
from callback import callback

username = os.getenv('RABBITMQ_USERNAME')
password = os.getenv('RABBITMQ_PASSWORD')

def consume(host):
    """Consumes messages from the 'router_jobs' queue."""
    for attempt in range(10):
        try:
            print(f"Connecting to RabbitMQ (try {attempt})...")

            credentials = pika.PlainCredentials(username, password)
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(
                    host=host,
                    credentials=credentials
                )
            )
            break

        except Exception as e:
            print(f"Connection failed: {e}")
            time.sleep(5)
    else:
        print("Could not connect after 10 attempts, exiting..."); exit(1)

    channel = connection.channel()
    channel.queue_declare(queue="router_jobs")
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue="router_jobs", on_message_callback=callback, auto_ack=True)
    channel.start_consuming()

if __name__ == "__main__":
    consume("localhost")
