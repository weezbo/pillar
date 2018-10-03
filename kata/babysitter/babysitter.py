
def calculate_total_for_period(hours, rate):
    return hours*rate;

def calculate_hours_for_period(start_time, end_time):
    start_hour = int(start_time[0:2])
    end_hour = int(end_time[0:2])
    end_minute = int(end_time[-2:])
    if end_minute > 0:
        end_hour += 1
    total_hours = end_hour - start_hour
    if total_hours < 1:
        total_hours = 1
    return total_hours
