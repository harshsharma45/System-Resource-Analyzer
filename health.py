# get health status.
def get_health_status(cpu, ram, disk):
    warnings = []

    if cpu > 85:
        warnings.append('⚠ HIGH CPU USAGE')

    if ram > 75:
        warnings.append('⚠ HIGH RAM USAGE')

    if disk > 85:
        warnings.append('⚠ LOW DISK SPACE')

    if not warnings:
        warnings.append('HEALTHY :)')

    return warnings

