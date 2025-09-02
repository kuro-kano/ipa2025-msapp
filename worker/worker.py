"""Worker that starts the consumer to process jobs from RabbitMQ. (I don't know why this file is needed)"""
from consumer import consume

consume("rabbitmq")
