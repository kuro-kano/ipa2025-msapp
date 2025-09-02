"""Worker that starts the consumer to process jobs from RabbitMQ."""
from consumer import consume
# Ok.. I knowed it a code runner..
consume("rabbitmq")
