import re, time

def temp_time(time_str: str) -> int:
    total_seconds = 0
    if time_str == "0":
        return None
    pattern = r'(\d+)\s*(d|h|min|s)'
    matches = re.findall(pattern, time_str)
    if not matches:
        return -1#
    else:
        for value, unit in matches:
            value = int(value)
            if unit == "d":
                total_seconds += value * 86400
            elif unit == "h":
                total_seconds += value * 3600
            elif unit == "min":
                total_seconds += value * 60
            elif unit == "s":
                total_seconds += value
            else:
                return None
    return int(time.time() + total_seconds)