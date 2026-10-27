from health import get_health_status
from ansi_escape_codes import GREEN, RED, RESET
from system_info import get_cpu_usage, get_ram_usage, get_disk_usage, format_uptime

# print the system health
line = '=' * 60

def display_system_health():
    cpu = get_cpu_usage()
    ram = get_ram_usage()
    disk = get_disk_usage()
    f_uptime = format_uptime()
    health_status = get_health_status(cpu, ram, disk)
    formatted_status = '\n'.join(health_status)
    

    if health_status == ['HEALTHY :)']:
        formatted_status = GREEN + formatted_status + RESET
    else:
        formatted_status = RED + formatted_status + RESET
        

    # multi-line string.
    print(f"""
{line}
                SYSTEM HEALTH CHECKER
{line}

CPU Usage     : {cpu}%
RAM Usage     : {ram}%
Disk Usage    : {disk}%
Uptime        : {f_uptime}
Health Status : \n{formatted_status}

{line}
""")