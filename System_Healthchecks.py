import psutil
import time


def monitor_system(interval=1):
    """
    Monitor CPU usage, disk usage, and memory utilization of the system.

    Parameters:
        interval (float): The time interval (in seconds) between each monitoring iteration.
    """
    try:
        print("Monitoring System:")

        while True:
            # Fetch CPU usage percentage
            cpu_percent = psutil.cpu_percent(interval=interval)
            print(f"CPU Usage: {cpu_percent}%")

            # Fetch disk usage information
            disk_usage = psutil.disk_usage('/')
            disk_total = disk_usage.total / (1024 * 1024 * 1024)  # Convert to GB
            disk_used = disk_usage.used / (1024 * 1024 * 1024)  # Convert to GB
            disk_percent = disk_usage.percent
            print(f"Disk Usage: Total: {disk_total:.2f} GB  Used: {disk_used:.2f} GB  Percentage: {disk_percent}%")

            # Fetch memory usage information
            mem_info = psutil.virtual_memory()
            mem_total = mem_info.total / (1024 * 1024 * 1024)  # Convert to GB
            mem_used = mem_info.used / (1024 * 1024 * 1024)  # Convert to GB
            mem_percent = mem_info.percent
            print(f"Memory Usage: Total: {mem_total:.2f} GB  Used: {mem_used:.2f} GB  Percentage: {mem_percent}%")

            time.sleep(interval)

    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")


if __name__ == "__main__":
    # Example usage: Monitor system
    monitor_system()
