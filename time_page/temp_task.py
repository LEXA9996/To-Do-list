import re, time

def temp_time(time_str: str):
    if time_str == "0":
        return None
    while True:
        pattern = r'(\d+)\s*(d|h|min|m|s)'
        matches = re.findall(pattern, time_str)
        if not matches:
            print("❌ Неверный формат времени. Пример: '1d 3h 20min'")
            continue
        break
    total_seconds = 0
    for value, unit in matches:
        value = int(value)
        if unit == "m":
            total_seconds += value * 2592000
        elif unit == "d":
            total_seconds += value * 86400
        elif unit == "h":
            total_seconds += value * 3600
        elif unit == "min":
            total_seconds += value * 60
        elif unit == "s":
            total_seconds += value
        else:
            print(f"⚠️ Неизвестная единица времени: {unit}")

    return int(time.time() + total_seconds)