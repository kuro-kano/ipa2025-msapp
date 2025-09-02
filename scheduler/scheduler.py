"""Simple scheduler that periodically sends messages to RabbitMQ."""
import time, pika 
from producer import produce

def scheduler():
    """Periodically sends a message to RabbitMQ every 10 seconds."""
    count = 0
    while True:
        now = time.time()
        now_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(now))
        print(f"[{now_str}] run #{count}")

        try:
            produce("localhost", "192.168.1.44")
        except Exception as e:
            print(e); time.sleeps(3)
        count += 1
        time.sleep(10)

if __name__ == "__main__":
    scheduler()

