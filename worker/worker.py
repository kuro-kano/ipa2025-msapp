"""Worker that starts the consumer to process jobs from RabbitMQ."""
from consumer import consume

consume("rabbitmq")
