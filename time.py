from datetime import datetime, timedelta

def get_hour_from_offset(offset):

    city_hour = offset / 60 / 60
    time = datetime.utcnow() + timedelta(hours=city_hour)

    return time.strftime('%H:%M')
