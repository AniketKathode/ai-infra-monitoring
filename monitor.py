import psutil
import time

try:
    while True:
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent

        print(f"CPU: {cpu}% | Memory: {memory}% | Disk: {disk}%")

        time.sleep(4)

except KeyboardInterrupt:
    print("\nMonitoring stopped by user.")
