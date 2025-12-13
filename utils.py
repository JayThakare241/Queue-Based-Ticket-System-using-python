DEFAULT_AVG_TIME = 5  # minutes per customer


def estimated_wait_minutes(position):
    """
    position = 0 means next in queue
    """
    avg_time = DEFAULT_AVG_TIME

    try:
        with open("avg_service_time.txt", "r") as f:
            avg_time = int(f.read().strip())
    except:
        avg_time = DEFAULT_AVG_TIME

    return position * avg_time
