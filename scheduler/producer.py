"""Module to send messages to a RabbitMQ exchange for job scheduling."""
import pika
import os


def produce(host, body):
    """
    Sends a message to the 'jobs' exchange with
    the routing key 'check_interfaces'.

    Args:
        host (str): RabbitMQ server hostname or IP.
        body (str): Message body to send.
    """
    credentials = pika.PlainCredentials(
        os.getenv('RABBITMQ_USER'),
        os.getenv('RABBITMQ_PASS')
    )

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=host,
            credentials=credentials
        )
    )
    channel = connection.channel()

    channel.exchange_declare(
        exchange="jobs", exchange_type="direct"
    )
    channel.queue_declare(queue="router_jobs")
    channel.queue_bind(
        queue="router_jobs",
        exchange="jobs",
        routing_key="check_interfaces"
    )
    channel.basic_publish(
        exchange="jobs",
        routing_key="check_interfaces",
        body=body
    )

    connection.close()


if __name__ == "__main__":
    produce("localhost", "192.168.1.44")
