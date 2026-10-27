import psutil
from datetime import datetime


# get CPU usage.
def get_cpu_usage():
   # return the result after 1 second.
   cpu_usage = psutil.cpu_percent(interval=1)  
   return cpu_usage
 

# get RAM usage.
def get_ram_usage():
   memory = psutil.virtual_memory()
   return memory.percent

# get disk usage.
def get_disk_usage():
   usage = psutil.disk_usage(path="C:/")
   return usage.percent


# get uptime.
def get_uptime():
   boot_time = psutil.boot_time()
   boot_datetime = datetime.fromtimestamp(boot_time)
   current_time = datetime.now()
   uptime = current_time - boot_datetime
   return uptime

def format_uptime():
   uptime = get_uptime()
   days = uptime.days
   hours = uptime.seconds // 3600
   remaining_seconds = uptime.seconds % 3600
   minutes = remaining_seconds // 60
   seconds = remaining_seconds % 60
   return f'{days} days, {hours} hours, {minutes} minutes, {seconds} seconds'