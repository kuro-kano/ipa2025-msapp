"""Simple scheduler that periodically sends Jobs to RabbitMQ."""
import time, os, pika

from bson import json_util
from producer import produce
from database import get_router_info

def scheduler():
    """Periodically sends a message to RabbitMQ every 10 seconds."""
    INTERVAL = 60.0
    next_run = time.monotonic()
    count = 0

    rabbitmq_host = os.getenv('RABBITMQ_HOST')

    while True:
        now = time.time()
        now_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(now))
        ms = int((now % 1) * 1000)
        now_str_with_ms = f"{now_str}.{ms:03d}"
        print(f"[{now_str_with_ms}] run #{count}")

        try:
            for data in get_router_info():
                body_bytes = json_util.dumps(data).encode("utf-8")
                produce(rabbitmq_host, body_bytes)
        except Exception as e:
            print(e); time.sleep(3)
        count += 1
        next_run += INTERVAL
        time.sleep(max(0.0, next_run - time.monotonic()))

if __name__ == "__main__":
    scheduler()

